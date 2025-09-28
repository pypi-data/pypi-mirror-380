#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2019-2025 A S Lewis
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation; either version 2.1 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


"""Download and livestream operation classes."""


# Import Gtk modules
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GObject


# Import other modules
import datetime
import json
import __main__
import os
import queue
import random
import re
import requests
import shutil
import signal
import subprocess
import sys
import threading
import time


# Import our modules
import formats
import mainapp
import media
import options
import ttutils
# Use same gettext translations
from mainapp import _

if mainapp.HAVE_FEEDPARSER_FLAG:
    import feedparser


# Debugging flag (calls ttutils.debug_time() at the start of every function)
DEBUG_FUNC_FLAG = False


# Decorator to add thread synchronisation to some functions in the
#   downloads.DownloadList object
_SYNC_LOCK = threading.RLock()

def synchronise(lock):
    def _decorator(func):
        def _wrapper(*args, **kwargs):
            lock.acquire()
            ret_value = func(*args, **kwargs)
            lock.release()
            return ret_value
        return _wrapper
    return _decorator


# Classes
class DownloadManager(threading.Thread):

    """Called by mainapp.TartubeApp.download_manager_continue().

    Based on the DownloadManager class in youtube-dl-gui.

    Python class to manage a download operation.

    Creates one or more downloads.DownloadWorker objects, each of which handles
    a single download.

    This object runs on a loop, looking for available workers and, when one is
    found, assigning them something to download. The worker completes that
    download and then waits for another assignment.

    Args:

        app_obj: The mainapp.TartubeApp object

        operation_type (str): 'sim' if channels/playlists should just be
            checked for new videos, without downloading anything. 'real' if
            videos should be downloaded (or not) depending on each media data
            object's .dl_sim_flag IV

            'custom_real' is like 'real', but with additional options applied
            (specified by a downloads.CustomDLManager object). A 'custom_real'
            operation is sometimes preceded by a 'custom_sim' operation (which
            is the same as a 'sim' operation, except that it is always followed
            by a 'custom_real' operation)

            For downloads launched from the Classic Mode tab, 'classic_real'
            for an ordinary download, or 'classic_custom' for a custom
            download. A 'classic_custom' operation is always preceded by a
            'classic_sim' operation (which is the same as a 'sim' operation,
            except that it is always followed by a 'classic_custom' operation)

        download_list_obj (downloads.DownloadManager): An ordered list of
            media data objects to download, each one represented by a
            downloads.DownloadItem object

        custom_dl_obj (downloads.CustomDLManager or None): The custom download
            manager that applies to this download operation. Only specified
            when 'operation_type' is 'custom_sim', 'custom_real', 'classic_sim'
            or 'classic_real'

            For 'custom_real' and 'classic_real', not specified if
            mainapp.TartubeApp.temp_stamp_buffer_dict or
            .temp_slice_buffer_dict are specified (because those values take
            priority)

    """


    # Standard class methods


    def __init__(self, app_obj, operation_type, download_list_obj, \
    custom_dl_obj):

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 139 __init__')

        super(DownloadManager, self).__init__()

        # IV list - class objects
        # -----------------------
        # The mainapp.TartubeApp object
        self.app_obj = app_obj
        # Each instance of this object, which represents a single download
        #   operation, creates its own options.OptionsParser object. That
        #   object convert the download options stored in
        #   downloads.DownloadWorker.options_list into a list of youtube-dl
        #   command line options
        self.options_parser_obj = None
        # An ordered list of media data objects to download, each one
        #   represented by a downloads.DownloadItem object
        self.download_list_obj = download_list_obj
        # The custom download manager (downloads.CustomDLManager) that applies
        #   to this download operation. Only specified when 'operation_type' is
        #   'custom_sim', 'custom_real', 'classic_sim' or 'classic_real'
        # For 'custom_real' and 'classic_real', not specified if
        #   mainapp.TartubeApp.temp_stamp_buffer_dict or
        #   .temp_slice_buffer_dict are specified (because those values take
        #   priority)
        self.custom_dl_obj = custom_dl_obj
        # List of downloads.DownloadWorker objects, each one handling one of
        #   several simultaneous downloads
        self.worker_list = []


        # IV list - other
        # ---------------
        # 'sim' if channels/playlists should just be checked for new videos,
        #   without downloading anything. 'real' if videos should be downloaded
        #   (or not) depending on each media data object's .dl_sim_flag IV
        # 'custom_real' is like 'real', but with additional options applied
        #   (specified by a downloads.CustomDLManager object). A 'custom_real'
        #   operation is sometimes preceded by a 'custom_sim' operation (which
        #   is the same as a 'sim' operation, except that it is always followed
        #   by a 'custom_real' operation)
        # For downloads launched from the Classic Mode tab, 'classic_real' for
        #   an ordinary download, or 'classic_custom' for a custom download. A
        #   'classic_custom' operation is always preceded by a 'classic_sim'
        #   operation (which is the same as a 'sim' operation, except that it
        #   is always followed by a 'classic_custom' operation)
        # This is the default value for the download operation, when it starts.
        #   If the user wants to add new download.DownloadItem objects during
        #   an operation, the code can call
        #   downloads.DownloadList.create_item() with a non-default value of
        #   operation_type
        self.operation_type = operation_type
        # Shortcut flag to test the operation type; True for 'classic_sim',
        #   'classic_real' and 'classic_custom'; False for all other values
        self.operation_classic_flag = False         # (Set below)

        # The time at which the download operation began (in seconds since
        #   epoch)
        self.start_time = int(time.time())
        # The time at which the download operation completed (in seconds since
        #   epoch)
        self.stop_time = None
        # The time (in seconds) between iterations of the loop in self.run()
        self.sleep_time = 0.25

        # Flag set to False if self.stop_download_operation() is called
        # The False value halts the main loop in self.run()
        self.running_flag = True
        # Flag set to True if the operation has been stopped manually by the
        #   user (via a call to self.stop_download_operation() or
        #   .stop_download_operation_soon()
        self.manual_stop_flag = False

        # Number of download jobs started (number of downloads.DownloadItem
        #   objects which have been allocated to a worker)
        self.job_count = 0
        # The current downloads.DownloadItem being handled by self.run()
        #   (stored in this IV so that anything can update the main window's
        #   progress bar, at any time, by calling self.nudge_progress_bar() )
        self.current_item_obj = None

        # On-going counts of how many videos have been downloaded (real and
        #   simulated, and including videos from which one or more clips have
        #   been extracted), how many clips have been extracted, how many video
        #   slices have been removed, and how much disc space has been consumed
        #   (in bytes), so that the operation can be auto-stopped, if required
        self.total_video_count = 0
        self.total_dl_count = 0
        self.total_sim_count = 0
        self.total_clip_count = 0
        self.total_slice_count = 0
        self.total_size_count = 0
        # Special count for media.Video objects which have already been
        #   checked/downloaded, and are being checked again (directly, for
        #   example after right-clicking the video)
        # If non-zero, prevents mainwin.NewbieDialogue from opening
        self.other_video_count = 0

        # If mainapp.TartubeApp.operation_convert_mode is set to any value
        #   other than 'disable', then a media.Video object whose URL
        #   represents a channel/playlist is converted into multiple new
        #   media.Video objects, one for each video actually downloaded
        # The original media.Video object is added to this list, via a call to
        #   self.mark_video_as_doomed(). At the end of the whole download
        #   operation, any media.Video object in this list is destroyed
        self.doomed_video_list = []

        # When the self.operation_type is 'classic_sim', we just compile a list
        #   of all videos detected. (A single URL may produce multiple videos)
        # A second download operation is due to be launched when this one
        #   finishes, with self.operation_type set to 'classic_custom'. During
        #   that operation, each of these video will be downloaded individually
        # The list is in groups of two, in the form
        #   [ parent_obj, json_dict ]
        # ...where 'parent_obj' is a 'dummy' media.Video object representing a
        #   video, channel or playlist, from which the metedata for a single
        #   video, 'json_dict', has been extracted
        self.classic_extract_list = []

        # Flag set to True when alternative performance limits currently apply,
        #   False when not. By checking the previous value (stored here)
        #   against the new one, we can see whether the period of alternative
        #   limits has started (or stopped)
        self.alt_limits_flag = self.check_alt_limits()
        # Alternative limits are checked every five minutes. The time (in
        #   minutes past the hour) at which the next check should be performed
        self.alt_limits_check_time = None


        # Code
        # ----

        # Set the flag
        if operation_type == 'classic_sim' \
        or operation_type == 'classic_real' \
        or operation_type == 'classic_custom':
            self.operation_classic_flag = True

        # Create an object for converting download options stored in
        #   downloads.DownloadWorker.options_list into a list of youtube-dl
        #   command line options
        self.options_parser_obj = options.OptionsParser(self.app_obj)

        # Create a list of downloads.DownloadWorker objects, each one handling
        #   one of several simultaneous downloads
        # Note that if a downloads.DownloadItem was created by a
        #   media.Scheduled object that specifies more (or fewer) workers,
        #   then self.change_worker_count() will be called
        if self.alt_limits_flag:
            worker_count = self.app_obj.alt_num_worker
        elif self.app_obj.num_worker_apply_flag:
            worker_count = self.app_obj.num_worker_default
        else:
            worker_count = self.app_obj.num_worker_max

        for i in range(1, worker_count + 1):
            self.worker_list.append(DownloadWorker(self))

        # Set the time at which the first check for alternative limits is
        #   performed
        local = ttutils.get_local_time()
        self.alt_limits_check_time \
        = (int(int(local.strftime('%M')) / 5) * 5) + 5
        if self.alt_limits_check_time > 55:
            self.alt_limits_check_time = 0
        # (Also update the icon in the Progress tab)
        GObject.timeout_add(
            0,
            self.app_obj.main_win_obj.toggle_alt_limits_image,
            self.alt_limits_flag,
        )

        # Let's get this party started!
        self.start()


    # Public class methods


    def run(self):

        """Called as a result of self.__init__().

        On a continuous loop, passes downloads.DownloadItem objects to each
        downloads.DownloadWorker object, as they become available, until the
        download operation is complete.
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 319 run')

        manager_string = _('D/L Manager:') + '   '

        self.app_obj.main_win_obj.output_tab_write_stdout(
            0,
            manager_string + _('Starting download operation'),
        )

        # (Monitor changes to the number of workers, and number of available
        #   workers, so that we can display a running total in the Output tab's
        #   summary page)
        local_worker_available_count = 0
        local_worker_total_count = 0

        # Perform the download operation until there is nothing left to
        #   download, or until something has called
        #   self.stop_download_operation()
        while self.running_flag:

            # Send a message to the Output tab's summary page, if required.
            #   The number of workers shown doesn't include those dedicated to
            #   broadcasting livestreams
            available_count = 0
            total_count = 0
            for worker_obj in self.worker_list:
                if not worker_obj.broadcast_flag:
                    total_count += 1
                    if worker_obj.available_flag:
                        available_count += 1

            if local_worker_available_count != available_count \
            or local_worker_total_count != total_count:
                local_worker_available_count = available_count
                local_worker_total_count = total_count
                self.app_obj.main_win_obj.output_tab_write_stdout(
                    0,
                    manager_string + _('Workers: available:') + ' ' \
                    + str(available_count) + ', ' + _('total:') + ' ' \
                    + str(total_count),
                )

            # Auto-stop the download operation, if required
            for scheduled_obj in self.download_list_obj.scheduled_list:

                if scheduled_obj.autostop_time_flag:

                    # Calculate the current time limit, in seconds
                    unit = scheduled_obj.autostop_time_unit
                    time_limit = scheduled_obj.autostop_time_value \
                    * formats.TIME_METRIC_DICT[unit]

                    if (time.time() - self.start_time) > time_limit:
                        break

            if self.app_obj.autostop_time_flag:

                # Calculate the current time limit, in seconds
                time_limit = self.app_obj.autostop_time_value \
                * formats.TIME_METRIC_DICT[self.app_obj.autostop_time_unit]

                if (time.time() - self.start_time) > time_limit:
                    break

            # Every five minutes, check whether the period of alternative
            #   performance limits has started (or stopped)
            local = ttutils.get_local_time()
            if int(local.strftime('%M')) >= self.alt_limits_check_time:

                self.alt_limits_check_time += 5
                if self.alt_limits_check_time > 55:
                    self.alt_limits_check_time = 0

                new_flag = self.check_alt_limits()
                if new_flag != self.alt_limits_flag:

                    self.alt_limits_flag = new_flag
                    if not new_flag:

                        self.app_obj.main_win_obj.output_tab_write_stdout(
                            0,
                            _(
                            'Alternative performance limits no longer apply',
                            ),
                        )

                    else:

                        self.app_obj.main_win_obj.output_tab_write_stdout(
                            0,
                            _('Alternative performance limits now apply'),
                        )

                    # Change the number of workers. Bandwidth changes are
                    #   applied by OptionsParser.build_limit_rate()
                    if self.app_obj.num_worker_default \
                    != self.app_obj.alt_num_worker:

                        if not new_flag:

                            self.change_worker_count(
                                self.app_obj.num_worker_default,
                            )

                        else:

                            self.change_worker_count(
                                self.app_obj.alt_num_worker,
                            )

                    # (Also update the icon in the Progress tab)
                    GObject.timeout_add(
                        0,
                        self.app_obj.main_win_obj.toggle_alt_limits_image,
                        self.alt_limits_flag,
                    )

            # Fetch information about the next media data object to be
            #   downloaded (and store it in an IV, so the main window's
            #   progress bar can be updated at any time, by any code)
            self.current_item_obj = self.download_list_obj.fetch_next_item()

            # Exit this loop when there are no more downloads.DownloadItem
            #   objects whose .status is formats.MAIN_STAGE_QUEUED, and when
            #   all workers have finished their downloads
            # Otherwise, wait for an available downloads.DownloadWorker, and
            #   then assign the next downloads.DownloadItem to it
            if not self.current_item_obj:
                if self.check_workers_all_finished():

                    # Send a message to the Output tab's summary page
                    self.app_obj.main_win_obj.output_tab_write_stdout(
                        0,
                        manager_string + _('All threads finished'),
                    )

                    break

            else:
                worker_obj = self.get_available_worker(
                    self.current_item_obj.media_data_obj,
                )

                # If the worker has been marked as doomed (because the number
                #   of simultaneous downloads allowed has decreased) then we
                #   can destroy it now
                if worker_obj and worker_obj.doomed_flag:

                    worker_obj.close()
                    self.remove_worker(worker_obj)

                # Otherwise, initialise the worker's IVs for the next job
                elif worker_obj:

                    # Send a message to the Output tab's summary page
                    self.app_obj.main_win_obj.output_tab_write_stdout(
                        0,
                        _('Thread #') + str(worker_obj.worker_id) \
                        + ': ' + _('Downloading:') + ' \'' \
                        + self.current_item_obj.media_data_obj.name + '\'',
                    )

                    # Initialise IVs
                    worker_obj.prepare_download(self.current_item_obj)
                    # Change the download stage for that downloads.DownloadItem
                    self.download_list_obj.change_item_stage(
                        self.current_item_obj.item_id,
                        formats.MAIN_STAGE_ACTIVE,
                    )
                    # Update the main window's progress bar (but not for
                    #   workers dedicated to broadcasting livestreams)
                    if not worker_obj.broadcast_flag:
                        self.job_count += 1

                    # Throughout the downloads.py code, instead of calling a
                    #   mainapp.py or mainwin.py function directly (which is
                    #   not thread-safe), set a Glib timeout to handle it
                    if not self.operation_classic_flag:
                        self.nudge_progress_bar()

                    # If this downloads.DownloadItem was marked (while it was
                    #   still in the queue) as being the last one that should
                    #   be checked/downloaded, we can prevent any more items
                    #   being fetched from the downloads.DownloadList
                    if self.download_list_obj.final_item_id is not None \
                    and self.download_list_obj.final_item_id \
                    == self.current_item_obj.item_id:
                        self.download_list_obj.prevent_fetch_new_items()

            # Pause a moment, before the next iteration of the loop (don't want
            #   to hog resources)
            time.sleep(self.sleep_time)

        # Download operation complete (or has been stopped). Send messages to
        #   the Output tab's summary page
        self.app_obj.main_win_obj.output_tab_write_stdout(
            0,
            manager_string + _('Downloads complete (or stopped)'),
        )

        # Close all the workers
        self.app_obj.main_win_obj.output_tab_write_stdout(
            0,
            manager_string + _('Halting all workers'),
        )

        for worker_obj in self.worker_list:
            worker_obj.close()

        # Join and collect
        self.app_obj.main_win_obj.output_tab_write_stdout(
            0,
            manager_string + _('Join and collect threads'),
        )

        for worker_obj in self.worker_list:
            worker_obj.join()

        self.app_obj.main_win_obj.output_tab_write_stdout(
            0,
            manager_string + _('Operation complete'),
        )

        # Set the stop time
        self.stop_time = int(time.time())

        # Tell the Progress List (or Classic Progress List) to display any
        #   remaining download statistics immediately
        if not self.operation_classic_flag:

            GObject.timeout_add(
                0,
                self.app_obj.main_win_obj.progress_list_display_dl_stats,
            )

        else:

            GObject.timeout_add(
                0,
                self.app_obj.main_win_obj.classic_mode_tab_display_dl_stats,
            )

        # Any media.Video objects which have been marked as doomed, can now be
        #   destroyed
        for video_obj in self.doomed_video_list:
            self.app_obj.delete_video(
                video_obj,
                True,           # Delete any files associated with the video
                True,           # Don't update the Video Index yet
                True,           # Don't update the Video Catalogue yet
            )

        # (Also update the icon in the Progress tab)
        GObject.timeout_add(
            0,
            self.app_obj.main_win_obj.toggle_alt_limits_image,
            False,
        )

        # When youtube-dl reports it is finished, there is a short delay before
        #   the final downloaded video(s) actually exist in the filesystem
        # Therefore, mainwin.MainWin.progress_list_display_dl_stats() may not
        #   have marked the final video(s) as downloaded yet
        # Let the timer run for a few more seconds to allow those videos to be
        #   marked as downloaded (we can stop before that, if all the videos
        #   have been already marked)
        if not self.operation_classic_flag:

            GObject.timeout_add(
                0,
                self.app_obj.download_manager_halt_timer,
            )

        else:

            # For download operations launched from the Classic Mode tab, we
            #   don't need to wait at all
            GObject.timeout_add(
                0,
                self.app_obj.download_manager_finished,
            )


    def apply_ignore_limits(self):

        """Called by mainapp>TartubeApp.script_slow_timer_callback(), after
        starting a download operation to check/download everything.

        One of the media.Scheduled objects specified that operation limits
        should be ignored, so apply that setting to everything in the download
        list.

        (Doing things this way is a lot simpler than the alternatives.)
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 631 apply_ignore_limits')

        for item_id in self.download_list_obj.download_item_list:

            download_item_obj \
            = self.download_list_obj.download_item_dict[item_id]
            download_item_obj.set_ignore_limits_flag()


    def check_alt_limits(self):

        """Called by self.__init__() and .run().

        Checks whether alternative performance limits apply right now, or not.

        Return values:

            True if alternative limits apply, False if not

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 653 check_alt_limits')

        if not self.app_obj.alt_num_worker_apply_flag:
            return False

        # Get the current time and day of the week
        local = ttutils.get_local_time()
        current_hours = int(local.strftime('%H'))
        current_minutes = int(local.strftime('%M'))
        # 0=Monday, 6=Sunday
        current_day = local.today().weekday()
        target_day_str = self.app_obj.alt_day_string

        # The period of alternative performance limits have a start and stop
        #   time, stored as strings in the form '21:00'
        start_hours = int(self.app_obj.alt_start_time[0:2])
        start_minutes = int(self.app_obj.alt_start_time[3:5])
        stop_hours = int(self.app_obj.alt_stop_time[0:2])
        stop_minutes = int(self.app_obj.alt_stop_time[3:5])

        # Is the current time before or after the start/stop times?
        if current_hours < start_hours \
        or (current_hours == start_hours and current_minutes < start_minutes):
            start_before_flag = True
        else:
            start_before_flag = False

        if current_hours < stop_hours \
        or (current_hours == stop_hours and current_minutes < stop_minutes):
            stop_before_flag = True
        else:
            stop_before_flag = False

        # If the start time is earlier than the stop time, we assume they're on
        #   the same day
        if start_hours < stop_hours \
        or (start_hours == stop_hours and start_minutes < stop_minutes):

            if not ttutils.check_day(current_day, target_day_str) \
            or start_before_flag \
            or (not stop_before_flag):
                return False
            else:
                return True

        # Otherwise, we assume the stop time occurs the following day (e.g.
        #   21:00 to 07:00)
        else:

            prev_day = current_day - 1
            if prev_day < 0:
                prev_day = 6

            if (
                ttutils.check_day(current_day, target_day_str) \
                and (not start_before_flag)
            ) or (
                ttutils.check_day(prev_day, target_day_str) \
                and stop_before_flag
            ):
                return True
            else:
                return False


    def change_worker_count(self, number):

        """Called by mainapp.TartubeApp.set_num_worker_default(). Can also be
        called by self.run() when the period of alternative performances limits
        begins or ends.

        When the number of simultaneous downloads allowed is changed during a
        download operation, this function responds.

        If the number has increased, creates an extra download worker object.

        If the number has decreased, marks the worker as doomed. When its
        current download is completed, the download manager destroys it.

        Args:

            number (int): The new number of simultaneous downloads allowed

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 739 change_worker_count')

        # How many workers do we have already?
        current = len(self.worker_list)
        # If this object hasn't set up its worker pool yet, let the setup code
        #   proceed as normal
        # Sanity check: if the specified value is less than 1, or hasn't
        #   changed, take no action
        if not current or number < 1 or current == number:
            return

        # Usually, the number of workers goes up or down by one at a time, but
        #   we'll check for larger leaps anyway
        for i in range(1, (abs(current-number) + 1)):

            if number > current:

                # The number has increased. If any workers have marked as
                #   doomed, they can be unmarked, allowing them to continue
                match_flag = False

                for worker_obj in self.worker_list:
                    if worker_obj.doomed_flag:
                        worker_obj.set_doomed_flag(True)
                        match_flag = True
                        break

                if not match_flag:
                    # No workers were marked doomed, so create a brand new
                    #   download worker
                    self.worker_list.append(DownloadWorker(self))

            else:

                # The number has decreased. The first worker in the list is
                #   marked as doomed - that is, when it has finished its
                #   current job, it closes (rather than being given another
                #   job, as usual)
                for worker_obj in self.worker_list:
                    if not worker_obj.doomed_flag:
                        worker_obj.set_doomed_flag(True)
                        break


    def check_master_slave(self, media_data_obj):

        """Called by VideoDownloader.do_download().

        When two channels/playlists/folders share a download destination, we
        don't want to download both of them at the same time.

        This function is called when media_data_obj is about to be
        downloaded.

        Every worker is checked, to see if it's downloading to the same
        destination. If so, this function returns True, and
        VideoDownloader.do_download() waits a few seconds, before trying
        again.

        Otherwise, this function returns False, and
        VideoDownloader.do_download() is free to start its download.

        Args:

            media_data_obj (media.Channel, media.Playlist, media.Folder):
                The media data object that the calling function wants to
                download

        Return values:

            True or False, as described above

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 814 check_master_slave')

        for worker_obj in self.worker_list:

            if not worker_obj.available_flag \
            and worker_obj.download_item_obj:

                other_obj = worker_obj.download_item_obj.media_data_obj

                if other_obj.dbid != media_data_obj.dbid:

                    if (
                        not isinstance(other_obj, media.Video)
                        and other_obj.external_dir is not None
                    ):
                        if other_obj.external_dir \
                        == media_data_obj.external_dir:
                            return True

                    # (Alternative download destinations only apply when no
                    #   external directory is specified)
                    elif other_obj.dbid == media_data_obj.master_dbid:
                        return True

        return False


    def check_workers_all_finished(self):

        """Called by self.run().

        Based on DownloadManager._jobs_done().

        Return values:

            True if all downloads.DownloadWorker objects have finished their
                jobs, otherwise returns False

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 855 check_workers_all_finished')

        for worker_obj in self.worker_list:
            if not worker_obj.available_flag:
                return False

        return True


    def create_bypass_worker(self):

        """Called by downloads.DownloadList.create_item().

        For a broadcasting livestream, we create additional workers if
        required, possibly bypassing the limit specified by
        mainapp.TartubeApp.num_worker_default.
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 874 create_bypass_worker')

        # How many workers do we have already?
        current = len(self.worker_list)
        # If this object hasn't set up its worker pool yet, let the setup code
        #   proceed as normal
        if not current:
            return

        # If we don't already have the maximum number of workers (or if no
        #   limit currently applies), then we don't need to create any more
        if not self.app_obj.num_worker_apply_flag \
        or current < self.app_obj.num_worker_default:
            return

        # Check the existing workers, in case one is already available
        for worker_obj in self.worker_list:
            if worker_obj.available_flag:
                return

        # Bypass the worker limit to create an additional worker, to be used
        #   only for broadcasting livestreams
        self.worker_list.append(DownloadWorker(self, True))
        # Create an additional page in the main window's Output tab, if
        #   required
        GObject.timeout_add(
            0,
            self.app_obj.main_win_obj.output_tab_setup_pages,
        )


    def get_available_worker(self, media_data_obj):

        """Called by self.run().

        Based on DownloadManager._get_worker().

        Args:

            media_data_obj (media.Video, media.Channel, media.Playlist or
                media.Folder): The media data object which is the next to be
                downloaded

        Return values:

            The first available downloads.DownloadWorker, or None if there are
                no available workers

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 922 get_available_worker')

        # Some workers are only available when media_data_obj is media.Video
        #   that's a broadcasting livestream
        if isinstance(media_data_obj, media.Video) \
        and media_data_obj.live_mode == 2:
            broadcast_flag = True
        else:
            broadcast_flag = False

        for worker_obj in self.worker_list:

            if worker_obj.available_flag \
            and (broadcast_flag or not worker_obj.broadcast_flag):
                return worker_obj

        return None


    def mark_video_as_doomed(self, video_obj):

        """Called by VideoDownloader.check_dl_is_correct_type().

        When youtube-dl reports the URL associated with a download item
        object contains multiple videos (or potentially contains multiple
        videos), then the URL represents a channel or playlist, not a video.

        If the channel/playlist was about to be downloaded into a media.Video
        object, then the calling function takes action to prevent it.

        It then calls this function to mark the old media.Video object to be
        destroyed, once the download operation is complete.

        Args:

            video_obj (media.Video): The video object whose URL is not a video,
                and which must be destroyed

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 963 mark_video_as_doomed')

        if isinstance(video_obj, media.Video) \
        and not video_obj in self.doomed_video_list:
            self.doomed_video_list.append(video_obj)


    def nudge_progress_bar(self):

        """Can be called by anything.

        Called by self.run() during the download operation.

        Also called by code in other files, just after that code adds a new
        media data object to our download list.

        Updates the main window's progress bar.
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 983 nudge_progress_bar')

        if self.current_item_obj:

            GObject.timeout_add(
                0,
                self.app_obj.main_win_obj.update_progress_bar,
                self.current_item_obj.media_data_obj.name,
                self.job_count,
                len(self.download_list_obj.download_item_list),
            )


    def register_classic_url(self, parent_obj, json_dict):

        """Called by VideoDownloader.extract_stdout_data().

        When the self.operation_type is 'classic_sim', we just compile a list
        of all videos detected.  (A single URL may produce multiple videos).

        A second download operation is due to be launched when this one
        finishes, with self.operation_type set to 'classic_custom'. During that
        operation, each of these URLs will be downloaded individually.

        Args:

            parent_obj (media.Video, media.Channel, media.Playlist): The
                media data object from which the URL was extracted

            json_dict (dict): Metadata extracted from a single video,
                stored as a dictionary

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 1018 register_classic_url')

        self.classic_extract_list.append(parent_obj)
        self.classic_extract_list.append(json_dict)


    def register_clip(self):

        """Called by ClipDownloader.confirm_video().

        A shorter version of self.register_video(). Clips do not count
        towards video limits, but we still keep track of them.

        When all of the clips for a video have been extracted, a further call
        to self.register_video() must be made.
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 1036 register_clip')

        self.total_clip_count += 1


    def register_slice(self):

        """Called by ClipDownloader.do_download_remove_slices().

        A shorter version of self.register_video(). Video slices removed from
        videos do not count towards video limits, but we still keep track of
        them.

        When all of the video sliceshave been removed, a further call to
        self.register_video() must be made.
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 1054 register_slice')

        self.total_slice_count += 1


    def register_video(self, dl_type):

        """Called by VideoDownloader.confirm_new_video(), when a video is
        downloaded, or by .confirm_sim_video(), when a simulated download finds
        a new video.

        Can also be called by .confirm_old_video() when downloading from the
        Classic Mode tab.

        Furthermore, called by ClipDownloader.do_download() when all clips for
        a video have been extracted, at least one of them successfully.

        This function adds the new video to its ongoing total and, if a limit
        has been reached, stops the download operation.

        Args:

            dl_type (str): 'new', 'sim', 'old', 'clip' or 'other', depending on
                the calling function

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 1082 register_video')

        if dl_type == 'other':
            # Special count for already checked/downloaded media.Videos, in
            #   order to prevent mainwin.NewbieDialogue opening
            self.other_video_count += 1

        else:
            self.total_video_count += 1
            if dl_type == 'new':
                self.total_dl_count += 1
            elif dl_type == 'sim':
                self.total_sim_count += 1

            for scheduled_obj in self.download_list_obj.scheduled_list:

                if scheduled_obj.autostop_videos_flag \
                and self.total_video_count \
                >= scheduled_obj.autostop_videos_value:
                    return self.stop_download_operation()

            if self.app_obj.autostop_videos_flag \
            and self.total_video_count >= self.app_obj.autostop_videos_value:
                self.stop_download_operation()


    def register_video_size(self, size=None):

        """Called by mainapp.TartubeApp.update_video_when_file_found().

        Called with the size of a video that's just been downloaded. This
        function adds the size to its ongoing total and, if a limit has been
        reached, stops the download operation.

        Args:

            size (int): The size of the downloaded video (in bytes)

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 1123 register_video_size')

        # (In case the filesystem didn't detect the file size, for whatever
        #   reason, we'll check for a None value)
        if size is not None:

            self.total_size_count += size

            for scheduled_obj in self.download_list_obj.scheduled_list:

                if scheduled_obj.autostop_size_flag:

                    # Calculate the current limit
                    unit = scheduled_obj.autostop_size_unit
                    limit = scheduled_obj.autostop_size_value \
                    * formats.FILESIZE_METRIC_DICT[unit]

                    if self.total_size_count >= limit:
                        return self.stop_download_operation()

            if self.app_obj.autostop_size_flag:

                # Calculate the current limit
                limit = self.app_obj.autostop_size_value \
                * formats.FILESIZE_METRIC_DICT[self.app_obj.autostop_size_unit]

                if self.total_size_count >= limit:
                    self.stop_download_operation()


    def remove_worker(self, worker_obj):

        """Called by self.run().

        When a worker marked as doomed has completed its download job, this
        function is called to remove it from self.worker_list.

        Args:

            worker_obj (downloads.DownloadWorker): The worker object to remove

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 1167 remove_worker')

        new_list = []

        for other_obj in self.worker_list:
            if other_obj != worker_obj:
                new_list.append(other_obj)

        self.worker_list = new_list


    def stop_download_operation(self):

        """Called by mainapp.TartubeApp.do_shutdown(), .stop_continue(),
        .dl_timer_callback(), .on_button_stop_operation().

        Also called by mainwin.StatusIcon.on_stop_menu_item().

        Also called by self.register_video() and .register_video_size().

        Based on DownloadManager.stop_downloads().

        Stops the download operation. On the next iteration of self.run()'s
        loop, the downloads.DownloadWorker objects are cleaned up.
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 1194 stop_download_operation')

        self.running_flag = False
        self.manual_stop_flag = True

        # In the Progress List, change the status of remaining items from
        #   'Waiting' to 'Not started'
        self.download_list_obj.abandon_remaining_items()


    def stop_download_operation_soon(self):

        """Called by mainwin.MainWin.on_progress_list_stop_all_soon(), after
        the user clicks the 'Stop after these videos' option in the Progress
        List.

        Stops the download operation, but only after any videos which are
        currently being downloaded have finished downloading.
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 1215 stop_download_operation_soon')

        self.manual_stop_flag = True

        self.download_list_obj.prevent_fetch_new_items()
        for worker_obj in self.worker_list:
            if worker_obj.running_flag \
            and worker_obj.downloader_obj is not None:
                worker_obj.downloader_obj.stop_soon()

        # In the Progress List, change the status of remaining items from
        #   'Waiting' to 'Not started'
        self.download_list_obj.abandon_remaining_items()


class DownloadWorker(threading.Thread):

    """Called by downloads.DownloadManager.__init__().

    Based on the Worker class in youtube-dl-gui.

    Python class for managing simultaneous downloads. The parent
    downloads.DownloadManager object can create one or more workers, each of
    which handles a single download.

    The download manager runs on a loop, looking for available workers and,
    when one is found, assigns them something to download.

    After the download is completely, the worker optionally checks a channel's
    or a playlist's RSS feed, looking for livestreams.

    When all tasks are completed, the worker waits for another assignment.

    Args:

        download_manager_obj (downloads.DownloadManager): The parent download
            manager object

        broadcast_flag (bool): True if this worker has been created
            specifically to handle broadcasting livestreams (see comments
            below); False if not

    """


    # Standard class methods


    def __init__(self, download_manager_obj, broadcast_flag=False):

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 1266 __init__')

        super(DownloadWorker, self).__init__()

        # IV list - class objects
        # -----------------------
        # The parent downloads.DownloadManager object
        self.download_manager_obj = download_manager_obj
        # The downloads.DownloadItem object for the current job
        self.download_item_obj = None
        # The downloads.VideoDownloader, downloads.ClipDownloader or
        #   downloads.StreamDownloader object for the current job (if it
        #   exists)
        self.downloader_obj = None
        # The downloads.JSONFetcher object for the current job (if it exists)
        self.json_fetcher_obj = None
        # The options.OptionsManager object for the current job
        self.options_manager_obj = None


        # IV list - other
        # ---------------
        # A number identifying this worker, matching the number of the page
        #   in the Output tab (so the first worker created is #1)
        self.worker_id = len(download_manager_obj.worker_list) + 1

        # The time (in seconds) between iterations of the loop in self.run()
        self.sleep_time = 0.25

        # Flag set to False if self.close() is called
        # The False value halts the main loop in self.run()
        self.running_flag = True
        # Flag set to True when the parent downloads.DownloadManager object
        #   wants to destroy this worker, having called self.set_doomed_flag()
        #   to do that
        # The worker is not destroyed until its current download is complete
        self.doomed_flag = False
        # Downloads of broadcasting livestreams must start as soon as possible.
        #   If the worker limit (mainapp.TartubeApp.num_worker_default) has
        #   been reached, additional workers are created to handle them
        # If True, this worker can only be used for broadcasting livestreams.
        #   If False, it can be used for anything
        self.broadcast_flag = broadcast_flag

        # Options list (used by downloads.VideoDownloader)
        # Initialised in the call to self.prepare_download()
        self.options_list = []
        # Flag set to True when the worker is available for a new job, False
        #   when it is already occupied with a job
        self.available_flag = True


        # Code
        # ----

        # Let's get this party started!
        self.start()


    # Public class methods


    def run(self):

        """Called as a result of self.__init__().

        Waits until this worker has been assigned a job, at which time we
        create a new downloads.VideoDownloader or downloads.StreamDownloader
        object and wait for the result.
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 1338 run')

        # Import the main application and custom download manager (for
        #   convenience)
        app_obj = self.download_manager_obj.app_obj
        custom_dl_obj = self.download_manager_obj.custom_dl_obj

        # Handle a job, or wait for the downloads.DownloadManager to assign
        #   this worker a job
        while self.running_flag:

            # If this worker is currently assigned a job...
            if not self.available_flag:

                # Import the media data object (for convenience)
                media_data_obj = self.download_item_obj.media_data_obj

                # If the downloads.DownloadItem was created by a scheduled
                #   download (media.Scheduled), then change the number of
                #   workers, if necessary
                if self.download_item_obj.scheduled_obj:

                    scheduled_obj = self.download_item_obj.scheduled_obj
                    if scheduled_obj.scheduled_num_worker_apply_flag \
                    and scheduled_obj.scheduled_num_worker \
                    != len(self.download_manager_obj.worker_list):

                        self.download_manager_obj.change_worker_count(
                            scheduled_obj.scheduled_num_worker,
                        )

                # When downloading a livestream that's broadcasting now, we
                #   call StreamDownloader rather than VideoDownloader
                # When downloading video clips, use youtube-dl with FFmpeg as
                #   its external downloader
                # Otherwise, use youtube-dl with an argument list determined by
                #   the download options applied
                if isinstance(media_data_obj, media.Video) \
                and media_data_obj.live_mode == 2 \
                and self.download_item_obj.operation_type != 'sim' \
                and self.download_item_obj.operation_type != 'custom_sim' \
                and self.download_item_obj.operation_type != 'classic_sim':
                    self.run_stream_downloader(media_data_obj)

                elif isinstance(media_data_obj, media.Video) \
                and not media_data_obj.live_mode \
                and (
                    (
                        (
                            self.download_item_obj.operation_type \
                            == 'custom_real' \
                            or self.download_item_obj.operation_type \
                            == 'classic_custom'
                        ) and (
                            (
                                custom_dl_obj \
                                and custom_dl_obj.dl_by_video_flag \
                                and custom_dl_obj.split_flag
                                and media_data_obj.stamp_list
                            ) or (
                                custom_dl_obj \
                                and custom_dl_obj.dl_by_video_flag \
                                and not custom_dl_obj.split_flag \
                                and custom_dl_obj.slice_flag
                                and media_data_obj.slice_list
                            ) or media_data_obj.dbid in \
                            app_obj.temp_stamp_buffer_dict \
                            or media_data_obj.dbid in \
                            app_obj.temp_slice_buffer_dict \
                        )
                    ) or (
                        self.download_item_obj.operation_type \
                        == 'classic_real' \
                        and media_data_obj.dbid in \
                        app_obj.temp_stamp_buffer_dict
                    )
                ):
                    self.run_clip_slice_downloader(media_data_obj)

                else:
                    self.run_video_downloader(media_data_obj)

                # Send a message to the Output tab's summary page
                app_obj.main_win_obj.output_tab_write_stdout(
                    0,
                    _('Thread #') + str(self.worker_id) \
                    + ': ' + _('Job complete') + ' \'' \
                    + self.download_item_obj.media_data_obj.name + '\'',
                )

                # This worker is now available for a new job
                self.available_flag = True

                # Send a message to the Output tab's summary page
                app_obj.main_win_obj.output_tab_write_stdout(
                    0,
                    _('Thread #') + str(self.worker_id) \
                    + ': ' + _('Worker now available again'),
                )

                # During (real, not simulated) custom downloads, apply a delay
                #   if one has been specified
                if (
                    self.download_item_obj.operation_type == 'custom_real' \
                    or self.download_item_obj.operation_type \
                    == 'classic_custom'
                ) and custom_dl_obj \
                and custom_dl_obj.delay_flag:

                    # Set the delay (in seconds), a randomised value if
                    #   required
                    if custom_dl_obj.delay_min:
                        delay = random.randint(
                            int(custom_dl_obj.delay_min * 60),
                            int(custom_dl_obj.delay_max * 60),
                        )
                    else:
                        delay = int(custom_dl_obj.delay_max * 60)

                    time.sleep(delay)

            # Pause a moment, before the next iteration of the loop (don't want
            #   to hog resources)
            time.sleep(self.sleep_time)


    def run_video_downloader(self, media_data_obj):

        """Called by self.run()

        Creates a new downloads.VideoDownloader to handle the download(s) for
        this job, and destroys it when it's finished.

        If possible, checks the channel/playlist RSS feed for videos we don't
        already have, and mark them as livestreams

        Args:

            media_data_obj (media.Video, media.Channel, media.Playlist,
                media.Folder): The media data object being downloaded. When the
                download operation was launched from the Classic Mode tab, a
                dummy media.Video object

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 1484 run_video_downloader')

        # Import the main application (for convenience)
        app_obj = self.download_manager_obj.app_obj

        # If the download stalls, the VideoDownloader may need to be replaced
        #   with a new one. Use a while loop for that
        first_flag = True
        restart_count = 0

        while True:

            # Set up the new downloads.VideoDownloader object
            self.downloader_obj = VideoDownloader(
                self.download_manager_obj,
                self,
                self.download_item_obj,
            )

            if first_flag:

                first_flag = False
                # Send a message to the Output tab's summary page
                app_obj.main_win_obj.output_tab_write_stdout(
                    0,
                    _('Thread #') + str(self.worker_id) \
                    + ': ' + _('Assigned job:') + ' \'' \
                    + self.download_item_obj.media_data_obj.name \
                    + '\'',
                )

            # Execute the assigned job
            return_code = self.downloader_obj.do_download()

            # Any youtube-dl error/warning messages which have not yet been
            #   passed to their media.Video objects can now be processed
            for vid in self.downloader_obj.video_msg_buffer_dict.keys():
                self.downloader_obj.process_error_warning(vid)

            # Unless the download was stopped manually (return code 5), any
            #   'dummy' media.Video objects can be set, so that their URLs are
            #   not remembered in the next Tartube session
            if isinstance(media_data_obj, media.Video) \
            and media_data_obj.dummy_flag \
            and return_code < 5:
                media_data_obj.set_dummy_dl_flag(True)

            # If the download stalled, -1 is returned. If we're allowed to
            #   restart a stalled download, do that; otherwise give up
            if return_code > -1 \
            or (
                app_obj.operation_auto_restart_max != 0
                and restart_count >= app_obj.operation_auto_restart_max
            ):
                break

            else:
                restart_count += 1
                msg = _('Tartube is restarting a stalled download')

                # Show confirmation of the restart
                if app_obj.ytdl_output_stdout_flag:
                    app_obj.main_win_obj.output_tab_write_stdout(
                        self.worker_id,
                        msg,
                    )

                if app_obj.ytdl_write_stdout_flag:
                    print(msg)

                if app_obj.ytdl_log_stdout_flag:
                    app_obj.write_downloader_log(msg)

        # If the downloads.VideoDownloader object collected any youtube-dl
        #   error/warning messages, display them in the Error List
        if media_data_obj.error_list or media_data_obj.warning_list:
            GObject.timeout_add(
                0,
                app_obj.main_win_obj.errors_list_add_operation_msg,
                media_data_obj,
            )

        # In the event of an error, nothing updates the video's row in the
        #   Video Catalogue, and therefore the error icon won't be visible
        # Do that now (but don't if mainwin.ComplexCatalogueItem objects aren't
        #   being used in the Video Catalogue)
        if not self.download_item_obj.operation_classic_flag \
        and return_code == VideoDownloader.ERROR \
        and isinstance(media_data_obj, media.Video) \
        and app_obj.catalogue_mode_type != 'simple':
            GObject.timeout_add(
                0,
                app_obj.main_win_obj.video_catalogue_update_video,
                media_data_obj,
            )

        # Call the destructor function of VideoDownloader object
        self.downloader_obj.close()

        # If possible, check the channel/playlist RSS feed for videos we don't
        #   already have, and mark them as livestreams
        if self.running_flag \
        and mainapp.HAVE_FEEDPARSER_FLAG \
        and app_obj.enable_livestreams_flag \
        and (
            isinstance(media_data_obj, media.Channel) \
            or isinstance(media_data_obj, media.Playlist)
        ) and not media_data_obj.dl_no_db_flag \
        and media_data_obj.child_list \
        and media_data_obj.rss:

            # Send a message to the Output tab's summary page
            app_obj.main_win_obj.output_tab_write_stdout(
                0,
                _('Thread #') + str(self.worker_id) \
                + ': ' + _('Checking RSS feed'),
            )

            # Check the RSS feed for the media data object
            self.check_rss(media_data_obj)


    def run_clip_slice_downloader(self, media_data_obj):

        """Called by self.run()

        Creates a new downloads.ClipDownloader to handle the download(s) for
        this job, and destroys it when it's finished.

        Args:

            media_data_obj (media.Video): The media data object being
                downloaded. When the download operation was launched from the
                Classic Mode tab, a dummy media.Video object

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 1622 run_clip_slice_downloader')

        # Import the main application and custom download manager (for
        #   convenience)
        app_obj = self.download_manager_obj.app_obj
        custom_dl_obj = self.download_manager_obj.custom_dl_obj

        # Set up the new downloads.ClipDownloader object
        self.downloader_obj = ClipDownloader(
            self.download_manager_obj,
            self,
            self.download_item_obj,
        )

        # Send a message to the Output tab's summary page
        app_obj.main_win_obj.output_tab_write_stdout(
            0,
            _('Thread #') + str(self.worker_id) \
            + ': ' + _('Assigned job:') + ' \'' \
            + self.download_item_obj.media_data_obj.name \
            + '\'',
        )

        # Execute the assigned job
        # ClipDownloader handles two related operations. Both start by
        #   downloading the video as clips. The second operation concatenates
        #   the clips back together, which has the effect of removing one or
        #   more slices from a video
        if (
            custom_dl_obj \
            and custom_dl_obj.split_flag \
            and media_data_obj.stamp_list
        ) or media_data_obj.dbid in app_obj.temp_stamp_buffer_dict:
            return_code = self.downloader_obj.do_download_clips()
        else:
            return_code = self.downloader_obj.do_download_remove_slices()

        # In the event of an error, nothing updates the video's row in the
        #   Video Catalogue, and therefore the error icon won't be visible
        # Do that now (but don't if mainwin.ComplexCatalogueItem objects aren't
        #   being used in the Video Catalogue)
        if not self.download_item_obj.operation_classic_flag \
        and return_code == ClipDownloader.ERROR \
        and app_obj.catalogue_mode_type != 'simple':
            GObject.timeout_add(
                0,
                app_obj.main_win_obj.video_catalogue_update_video,
                media_data_obj,
            )

        # Call the destructor function of ClipDownloader object
        self.downloader_obj.close()


    def run_stream_downloader(self, media_data_obj):

        """Called by self.run()

        A modified version of self.run_video_downloader(), used when
        downloading a media.Video object that's a livestream broadcasting now.

        First creates a new downloads.VideoDownloader to check the video, if
        it hasn't already been checked (which fetches the thumbnail,
        description, annotations and metadata files).

        Then creates a new downloads.StreamDownloader to handle the download
        for this job.

        Args:

            media_data_obj (media.Video): The media data object being
                downloaded

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 1698 run_stream_downloader')

        # Import the main application (for convenience)
        app_obj = self.download_manager_obj.app_obj

        # Checking a livestream (simulated download), before downloading it
        #   (real download) makes sure that the thumbnail and other metadata
        #   files are downloaded, if required
        # Assume that the video has not been checked if its path or name are
        #   not set
        # If mainapp.TartubeApp.livestream_dl_mode is 'default', meaning that
        #   youtube-dl is downloading the livestream directly, then there is
        #   no need to check the video first
        if app_obj.livestream_dl_mode != 'default' \
        and not self.download_manager_obj.operation_classic_flag \
        and (
            app_obj.livestream_force_check_flag \
            or media_data_obj.file_name is None \
            or media_data_obj.file_ext is None
        ):
            # Set up the new downloads.VideoDownloader object. The True
            #   argument forces it to do a simulated download
            self.downloader_obj = VideoDownloader(
                self.download_manager_obj,
                self,
                self.download_item_obj,
                True,
            )

            # Send a message to the Output tab's summary page
            app_obj.main_win_obj.output_tab_write_stdout(
                0,
                _('Thread #') + str(self.worker_id) \
                + ': ' + _('Assigned job:') + ' \'' \
                + self.download_item_obj.media_data_obj.name \
                + '\'',
            )

            # Execute the assigned job (but regardless of success or failure,
            #   we press on with the livestream download below)
            return_code = self.downloader_obj.do_download()

            # Any youtube-dl error/warning messages which have not yet been
            #   passed to their media.Video objects can now be processed
            for vid in self.downloader_obj.video_msg_buffer_dict.keys():
                self.downloader_obj.process_error_warning(vid)

            # If the downloads.VideoDownloader object collected any youtube-dl
            #   error/warning messages, display them in the Error List
            if media_data_obj.error_list or media_data_obj.warning_list:
                GObject.timeout_add(
                    0,
                    app_obj.main_win_obj.errors_list_add_operation_msg,
                    media_data_obj,
                )

            # In the event of an error, nothing updates the video's row in the
            #   Video Catalogue, and therefore the error icon won't be visible
            # Do that now (but don't if mainwin.ComplexCatalogueItem objects
            #   aren't being used in the Video Catalogue)
            if not self.download_item_obj.operation_classic_flag \
            and return_code == VideoDownloader.ERROR \
            and isinstance(media_data_obj, media.Video) \
            and app_obj.catalogue_mode_type != 'simple':
                GObject.timeout_add(
                    0,
                    app_obj.main_win_obj.video_catalogue_update_video,
                    media_data_obj,
                )

            # Call the destructor function of VideoDownloader object
            self.downloader_obj.close()

            # In the event of an error during the checking stage, don't
            #   proceed with the download
            if return_code >= VideoDownloader.ERROR:
                return

            # Reset our IVs, ready for the call to StreamDownloader
            self.prepare_download(self.download_item_obj)

        # Now proceed with the livestream download. Set up the new
        #   downloads.StreamDownloader object
        self.downloader_obj = StreamDownloader(
            self.download_manager_obj,
            self,
            self.download_item_obj,
        )

        # Send a message to the Output tab's summary page
        app_obj.main_win_obj.output_tab_write_stdout(
            0,
            _('Thread #') + str(self.worker_id) \
            + ': ' + _('Assigned job:') + ' \'' \
            + self.download_item_obj.media_data_obj.name \
            + '\'',
        )

        # Execute the assigned job
        return_code = self.downloader_obj.do_download()

        # In the event of an error, nothing updates the video's row in the
        #   Video Catalogue, and therefore the error icon won't be visible
        # Do that now (but don't if mainwin.ComplexCatalogueItem objects aren't
        #   being used in the Video Catalogue)
        if not self.download_item_obj.operation_classic_flag \
        and return_code == StreamDownloader.ERROR \
        and app_obj.catalogue_mode_type != 'simple':
            GObject.timeout_add(
                0,
                app_obj.main_win_obj.video_catalogue_update_video,
                media_data_obj,
            )

        # Call the destructor function of StreamDownloader object
        self.downloader_obj.close()


    def close(self):

        """Called by downloads.DownloadManager.run().

        This worker object is closed when:

            1. The download operation is complete (or has been stopped)
            2. The worker has been marked as doomed, and the calling function
                is now ready to destroy it

        Tidy up IVs and stop any child processes.
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 1830 close')

        self.running_flag = False

        if self.downloader_obj:
            self.downloader_obj.stop()

        if self.json_fetcher_obj:
            self.json_fetcher_obj.stop()


    def check_rss(self, container_obj):

        """Called by self.run(), after the VideoDownloader has finished.

        If possible, check the channel/playlist RSS feed for videos we don't
        already have, and mark them as livestreams.

        This process works on YouTube (each media.Channel and media.Playlist
        has the URL for its RSS feed set automatically).

        It might work on other compatible websites (the user must set the
        channel's/playlist's RSS feed manually).

        On a compatible website, when youtube-dl fetches a list of videos in
        the channel/playlist, it won't fetch any that are livestreams (either
        waiting to start, or currently broadcasting).

        However, livestreams (both waiting and broadcasting) do appear in the
        RSS feed. We can compare the RSS feed against the channel's/playlist's
        list of child media.Video objects (which has just been updated), in
        order to detect livestreams (with reasonably good accuracy).

        Args:

            container_obj (media.Channel, media.Playlist): The channel or
                playlist which the VideoDownloader has just checked/downloaded.
                (This function is not called for media.Folders or for
                individual media.Video objects)

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 1873 check_rss')

        app_obj = self.download_manager_obj.app_obj

        # Livestreams are usually the first entry in the RSS feed, having not
        #   started yet (or being currently broadcast), but there's no
        #   gurantee of that
        # In addition, although RSS feeds are normally quite short (with
        #    dozens of entries, not thousands), there is no guarantee of this
        # mainapp.TartubeApp.livestream_max_days specifies how many days of
        #   videos we should check, looking for livestreams
        # Implement this by stopping when an entry in the RSS feed matches a
        #   particular media.Video object
        # (If we can't decide which video to match, the default to searching
        #   the whole RSS feed)
        time_limit_video_obj = None
        check_source_list = []
        check_name_list = []

        if app_obj.livestream_max_days:

            # Stop checking the RSS feed at the first matching video that's
            #   older than the specified time
            # (Of course, the 'first video' must not itself be a livestream)
            older_time = int(
                time.time() - (app_obj.livestream_max_days * 86400),
            )

            for child_obj in container_obj.child_list:

                # An entry in the RSS feed is a new livestream, if it doesn't
                #   match one of the videos in these lists
                # (We don't need to check each RSS entry against the entire
                #   contents of the channel/playlist - which might be thousands
                #   of videos - just those up to the time limit)
                if child_obj.source:
                    check_source_list.append(child_obj.source)
                if child_obj.name != app_obj.default_video_name:
                    check_name_list.append(child_obj.name)

            # The time limit will apply to this video, when found
            for child_obj in container_obj.child_list:
                if child_obj.source \
                and not child_obj.live_mode \
                and child_obj.upload_time is not None \
                and child_obj.upload_time < older_time:
                    time_limit_video_obj = child_obj
                    break

        else:

            # Stop checking the RSS feed at the first matching video, no matter
            #   how old
            for child_obj in container_obj.child_list:
                if child_obj.source:
                    check_source_list.append(child_obj.source)
                if child_obj.name != app_obj.default_video_name:
                    check_name_list.append(child_obj.name)

            for child_obj in container_obj.child_list:
                if child_obj.source \
                and not time_limit_video_obj \
                and not child_obj.live_mode:
                    time_limit_video_obj = child_obj
                    break

        # Fetch the RSS feed
        try:
            feed_dict = feedparser.parse(container_obj.rss)
        except:
            return

        # Check each entry in the feed, stopping at the first one which matches
        #   the selected media.Video object
        for entry_dict in feed_dict['entries']:

            if time_limit_video_obj \
            and entry_dict['link'] == time_limit_video_obj.source:

                # Found a matching media.Video object, so we can stop looking
                #   for livestreams now
                break

            elif not entry_dict['link'] in check_source_list \
            and not entry_dict['title'] in check_name_list:

                # New livestream detected. Create a new JSONFetcher object to
                #   fetch its JSON data
                # If the data is received, the livestream is live. If the data
                #   is not received, the livestream is waiting to go live
                self.json_fetcher_obj = JSONFetcher(
                    self.download_manager_obj,
                    self,
                    container_obj,
                    entry_dict,
                )

                # Then execute the assigned job
                self.json_fetcher_obj.do_fetch()

                # Call the destructor function of the JSONFetcher object
                self.json_fetcher_obj.close()
                self.json_fetcher_obj = None


    def prepare_download(self, download_item_obj):

        """Called by downloads.DownloadManager.run().

        Also called by self.run_stream_downloader() after the checking phase,
        just before downloading the broadcasting livestream for real.

        Based on Worker.download().

        Updates IVs for a new job, so that self.run can initiate the download.

        Args:

            download_item_obj (downloads.DownloadItem): The download item
                object describing the URL from which youtube-dl should download
                video(s).

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 1998 prepare_download')

        self.download_item_obj = download_item_obj
        self.options_manager_obj = download_item_obj.options_manager_obj

        self.options_list = self.download_manager_obj.options_parser_obj.parse(
            self.download_item_obj.media_data_obj,
            self.options_manager_obj,
            self.download_item_obj.operation_type,
            self.download_item_obj.scheduled_obj,
        )

        self.available_flag = False


    def set_doomed_flag(self, flag):

        """Called by downloads.DownloadManager.change_worker_count()."""

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 2018 set_doomed_flag')

        self.doomed_flag = flag


    # Callback class methods


    def data_callback(self, dl_stat_dict, last_flag=False):

        """Called by downloads.VideoDownloader.read_child_process() and
        .last_data_callback().

        Based on Worker._data_hook() and ._talk_to_gui().

        'dl_stat_dict' holds a dictionary of statistics in a standard format
        specified by downloads.VideoDownloader.extract_stdout_data().

        This callback receives that dictionary and passes it on to the main
        window, so the statistics can be displayed there.

        Args:

            dl_stat_dict (dict): The dictionary of statistics described above

            last_flag (bool): True when called by .last_data_callback(),
                meaning that the VideoDownloader object has finished, and is
                sending this function the final set of statistics

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 2050 data_callback')

        main_win_obj = self.download_manager_obj.app_obj.main_win_obj

        if not self.download_item_obj.operation_classic_flag:

            GObject.timeout_add(
                0,
                main_win_obj.progress_list_receive_dl_stats,
                self.download_item_obj,
                dl_stat_dict,
                last_flag,
            )

            # If downloading a video individually, need to update the tooltips
            #   in the Results List to show any errors/warnings (which won't
            #   show up if the video was not downloaded)
            if last_flag \
            and isinstance(self.download_item_obj.media_data_obj, media.Video):

                GObject.timeout_add(
                    0,
                    main_win_obj.results_list_update_tooltip,
                    self.download_item_obj.media_data_obj,
                )

        else:

            GObject.timeout_add(
                0,
                main_win_obj.classic_mode_tab_receive_dl_stats,
                self.download_item_obj,
                dl_stat_dict,
                last_flag,
            )


class DownloadList(object):

    """Called by mainapp.TartubeApp.download_manager_continue().

    Based on the DownloadList class in youtube-dl-gui.

    Python class to keep track of all the media data objects to be downloaded
    (for real or in simulation) during a downloaded operation.

    This object contains an ordered list of downloads.DownloadItem objects.
    Each of those objects represents a media data object to be downloaded
    (media.Video, media.Channel, media.Playlist or media.Folder).

    Videos are downloaded in the order specified by the list.

    Args:

        app_obj (mainapp.TartubeApp): The main application

        operation_type (str): 'sim' if channels/playlists should just be
            checked for new videos, without downloading anything. 'real' if
            videos should be downloaded (or not) depending on each media data
            object's .dl_sim_flag IV

            'custom_real' is like 'real', but with additional options applied
            (specified by a downloads.CustomDLManager object). A 'custom_real'
            operation is sometimes preceded by a 'custom_sim' operation (which
            is the same as a 'sim' operation, except that it is always followed
            by a 'custom_real' operation)

            For downloads launched from the Classic Mode tab, 'classic_real'
            for an ordinary download, or 'classic_custom' for a custom
            download. A 'classic_custom' operation is always preceded by a
            'classic_sim' operation (which is the same as a 'sim' operation,
            except that it is always followed by a 'classic_custom' operation)

        media_data_list (list): List of media.Video, media.Channel,
            media.Playlist and/or media.Folder objects. Can also be a list of
            (exclusively) media.Scheduled objects. If not an empty list, only
            the specified media data objects (and their children) are
            checked/downloaded. If an empty list, all media data objects are
            checked/downloaded. If operation_type is 'classic', then the
            media_data_list contains a list of dummy media.Video objects from a
            previous call to this function. If an empty list, all
            dummy media.Video objects are downloaded

        custom_dl_obj (downloads.CustomDLManager or None): The custom download
            manager that applies to this download operation. Only specified
            when 'operation_type' is 'custom_sim', 'custom_real', 'classic_sim'
            or 'classic_real'

            For 'custom_real' and 'classic_real', not specified if
            mainapp.TartubeApp.temp_stamp_buffer_dict or
            .temp_slice_buffer_dict are specified (because those values take
            priority)

    """


    # Standard class methods


    def __init__(self, app_obj, operation_type, media_data_list, \
    custom_dl_obj):

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 2153 __init__')

        # IV list - class objects
        # -----------------------
        self.app_obj = app_obj

        # The custom download manager (downloads.CustomDLManager) that applies
        #   to this download operation. Only specified when 'operation_type' is
        #   'custom_sim', 'custom_real', 'classic_sim' or 'classic_real'
        # For 'custom_real' and 'classic_real', not specified if
        #   mainapp.TartubeApp.temp_stamp_buffer_dict or
        #   .temp_slice_buffer_dict are specified (because those values take
        #   priority)
        self.custom_dl_obj = custom_dl_obj

        # IV list - other
        # ---------------
        # 'sim' if channels/playlists should just be checked for new videos,
        #   without downloading anything. 'real' if videos should be downloaded
        #   (or not) depending on each media data object's .dl_sim_flag IV
        # 'custom_real' is like 'real', but with additional options applied
        #   (specified by a downloads.CustomDLManager object). A 'custom_real'
        #   operation is sometimes preceded by a 'custom_sim' operation (which
        #   is the same as a 'sim' operation, except that it is always followed
        #   by a 'custom_real' operation)
        # For downloads launched from the Classic Mode tab, 'classic_real' for
        #   an ordinary download, or 'classic_custom' for a custom download. A
        #   'classic_custom' operation is always preceded by a 'classic_sim'
        #   operation (which is the same as a 'sim' operation, except that it
        #   is always followed by a 'classic_custom' operation)
        # This IV records the default setting for this operation. Once the
        #   download operation starts, new download.DownloadItem objects can
        #   be added to the list in a call to self.create_item(), and that call
        #   can specify a value that overrides the default value, just for that
        #   call
        # Overriding the default value is not possible for download operations
        #   initiated from the Classic Mode tab
        self.operation_type = operation_type
        # Shortcut flag to test the operation type; True for 'classic_sim',
        #   'classic_real' and 'classic_custom'; False forall other values
        self.operation_classic_flag = False         # (Set below)
        # Flag set to True in a call to self.prevent_fetch_new_items(), in
        #   which case subsequent calls to self.fetch_next_item() return
        #   nothing, preventing any further downloads
        self.prevent_fetch_flag = False

        # Number of download.DownloadItem objects created (used to give each a
        #   unique ID)
        self.download_item_count = 0

        # An ordered list of downloads.DownloadItem objects, one for each
        #   media.Video, media.Channel, media.Playlist or media.Folder object
        #   (including dummy media.Video objects used by download operations
        #   launched from the Classic Mode tab)
        # This list stores each item's .item_id
        self.download_item_list = []
        # A supplementary list of downloads.DownloadItem objects
        # Suppose self.download_item_list already contains items A B C, and
        #   some of part of the code wants to add items X Y Z to the beginning
        #   of the list, producing the list X Y Z A B C (and not Z Y X A B C)
        # The new items are added (one at a time) to this temporary list, and
        #   then added to the beginning/end of self.download_item_list at the
        #   end of this function (or in the next call to
        #   self.fetch_next_item() )
        self.temp_item_list = []

        # We preserve the 'media_data_list' argument (which may be an empty
        #   list). Used by mainapp.TartubeApp.download_manager_finished during
        #   a 'custom_sim' operation, in order to initiate the subsequent
        #   'custom_real' operation
        self.orig_media_data_list = media_data_list

        # Corresponding dictionary of downloads.DownloadItem items for quick
        #   lookup, containing items from both self.download_item_list and
        #   self.temp_item_list
        # Dictionary in the form
        #   key = download.DownloadItem.item_id
        #   value = the download.DownloadItem object itself
        self.download_item_dict = {}
        # The .item_id of a download.DownloadItem.item_id, which is set (if
        #   required) by a call to self.set_final_item()
        # When self.fetch_next_item() fetches this item, that item is the last
        #   item to be fetched: self.download_item_list() and
        #   self.temp_item_list() are emptied, and any items they contained are
        #   not checked/downloaded
        self.final_item_id = None

        # List of any media.Scheduled objects involved in the current download
        #   operation
        self.scheduled_list = []


        # Code
        # ----

        # Set the flag
        if operation_type == 'classic_sim' \
        or operation_type == 'classic_real' \
        or operation_type == 'classic_custom':
            self.operation_classic_flag = True

        # Compile the list

        # Scheduled downloads
        if media_data_list and isinstance(media_data_list[0], media.Scheduled):

            # media_data_list is a list of media.Scheduled objects, each one
            #   handling a scheduled download
            all_obj = False
            ignore_limits_flag = False

            for scheduled_obj in media_data_list:
                if scheduled_obj.all_flag:
                    all_obj = scheduled_obj
                if scheduled_obj.ignore_limits_flag:
                    ignore_limits_flag = True
                if all_obj:
                    break


            if all_obj:

                # Use all media data objects
                for dbid in self.app_obj.container_top_level_list:
                    obj = self.app_obj.media_reg_dict[dbid]
                    self.create_item(
                        obj,
                        all_obj,    # media.Scheduled object
                        None,       # override_operation_type
                        False,      # priority_flag
                        ignore_limits_flag,
                    )

            else:

                # Use only media data objects specified by the media.Scheduled
                #   objects
                # Don't add the same media data object twice
                check_dict = {}

                for scheduled_obj in media_data_list:

                    if scheduled_obj.join_mode == 'priority':
                        priority_flag = True
                    else:
                        priority_flag = False

                    for dbid in scheduled_obj.media_list:
                        if not dbid in check_dict:

                            obj = self.app_obj.media_reg_dict[dbid]
                            self.create_item(
                                obj,
                                scheduled_obj,
                                scheduled_obj.dl_mode,
                                priority_flag,
                                scheduled_obj.ignore_limits_flag,
                            )

                            check_dict[dbid] = None

        # Normal downloads
        elif not self.operation_classic_flag:

            # For each media data object to be downloaded, create a
            #   downloads.DownloadItem object, and update the IVs above
            if not media_data_list:

                # Use all media data objects
                for dbid in self.app_obj.container_top_level_list:
                    obj = self.app_obj.media_reg_dict[dbid]
                    self.create_item(
                        obj,
                        None,       # media.Scheduled object
                        None,       # override_operation_type
                        False,      # priority_flag
                        False,      # ignore_limits_flag
                    )

            else:

                for media_data_obj in media_data_list:

                    if isinstance(media_data_obj, media.Folder) \
                    and media_data_obj.priv_flag:

                        # Videos in a private folder's .child_list can't be
                        #   downloaded (since they are also a child of a
                        #   channel, playlist or a public folder)
                        GObject.timeout_add(
                            0,
                            app_obj.system_error,
                            301,
                            _('Cannot download videos in a private folder'),
                        )

                    else:

                        # Use the specified media data object
                        self.create_item(
                            media_data_obj,
                            None,       # media.Scheduled object
                            None,       # override_operation_type
                            False,      # priority_flag
                            False,      # ignore_limits_flag
                        )

            # Some media data objects have an alternate download destination,
            #   for example, a playlist ('slave') might download its videos
            #   into the directory used by a channel ('master')
            # This can increase the length of the operation, because a 'slave'
            #   won't start until its 'master' is finished
            # Make sure all designated 'masters' are handled before 'slaves' (a
            #   media data object can't be both a master and a slave)
            self.reorder_master_slave()

        # Downloads from the Classic Mode tab
        else:

            # The download operation was launched from the Classic Mode tab.
            #   Each URL to be downloaded is represented by a dummy media.Video
            #   object (one which is not in the media data registry)
            main_win_obj = self.app_obj.main_win_obj

            # The user may have rearranged rows in the Classic Mode tab, so
            #   get a list of (all) dummy media.Videos in the rearranged order
            # (It should be safe to assume that the Gtk.Liststore contains
            #   exactly the same number of rows, as dummy media.Video objects
            #   in mainwin.MainWin.classic_media_dict)
            dbid_list = []
            for row in main_win_obj.classic_progress_liststore:
                dbid_list.append(row[0])

            # Compile a list of dummy media.Video objects in the correct order
            obj_list = []
            if not media_data_list:

                # Use all of them
                for dbid in dbid_list:
                    obj_list.append(main_win_obj.classic_media_dict[dbid])

            else:

                # Use a subset of them
                for dbid in dbid_list:

                    dummy_obj = main_win_obj.classic_media_dict[dbid]
                    if dummy_obj in media_data_list:
                        obj_list.append(dummy_obj)


            # For each dummy media.Video object, create a
            #   downloads.DownloadItem object, and update the IVs above
            # Don't re-download a video already marked as downloaded (if the
            #   user actually wants to re-download a video, then
            #   mainapp.TartubeApp.on_button_classic_redownload() has reset the
            #   flag)
            for dummy_obj in obj_list:

                if not dummy_obj.dl_flag:
                    self.create_dummy_item(dummy_obj)

        # We can now merge the two DownloadItem lists
        if self.temp_item_list:

            self.download_item_list \
            = self.temp_item_list + self.download_item_list
            self.temp_item_list = []


    # Public class methods


    @synchronise(_SYNC_LOCK)
    def abandon_remaining_items(self):

        """Called by downloads.DownloadManager.stop_download_operation() and
        .stop_download_operation_soon().

        When the download operation has been stopped by the user, any rows in
        the main window's Progress List (or Classic Progress List) currently
        marked as 'Waiting' should be marked as 'Not started'.
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 2439 abandon_remaining_items')

        main_win_obj = self.app_obj.main_win_obj
        download_manager_obj = self.app_obj.download_manager_obj

        # In case of any recent calls to self.create_item(), which want to
        #   place new DownloadItems at the beginning of the queue, then
        #   merge the temporary queue into the main one
        if self.temp_item_list:
            self.download_item_list \
            = self.temp_item_list + self.download_item_list

        # 'dl_stat_dict' holds a dictionary of statistics in a standard format
        #   specified by downloads.VideoDownloader.extract_stdout_data()
        # Prepare the dictionary to be passed on to the main window, so the
        #   statistics can be displayed there for every 'Waiting' item
        dl_stat_dict = {}
        dl_stat_dict['status'] = formats.MAIN_STAGE_NOT_STARTED

        for item_id in self.download_item_list:
            this_item = self.download_item_dict[item_id]

            if this_item.stage == formats.MAIN_STAGE_QUEUED:
                this_item.stage = formats.MAIN_STAGE_NOT_STARTED

                if not download_manager_obj.operation_classic_flag:

                    GObject.timeout_add(
                        0,
                        main_win_obj.progress_list_receive_dl_stats,
                        this_item,
                        dl_stat_dict,
                        True,       # Final set of statistics for this item
                    )

                else:

                    GObject.timeout_add(
                        0,
                        main_win_obj.classic_mode_tab_receive_dl_stats,
                        this_item,
                        dl_stat_dict,
                        True,       # Final set of statistics for this item
                    )


    @synchronise(_SYNC_LOCK)
    def change_item_stage(self, item_id, new_stage):

        """Called by downloads.DownloadManager.run().

        Based on DownloadList.change_stage().

        Changes the download stage for the specified downloads.DownloadItem
        object.

        Args:

            item_id (int): The specified item's .item_id

            new_stage: The new download stage, one of the values imported from
                formats.py (e.g. formats.MAIN_STAGE_QUEUED)

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 2505 change_item_stage')

        self.download_item_dict[item_id].stage = new_stage


    def create_item(self, media_data_obj, scheduled_obj=None,
    override_operation_type=None, priority_flag=False,
    ignore_limits_flag=False, recursion_flag=False):

        """Called initially by self.__init__() (or by many other functions,
        for example in mainapp.TartubeApp).

        Subsequently called by this function recursively.

        Creates a downloads.DownloadItem object for media data objects in the
        media data registry.

        Doesn't create a download item object for:
            - media.Video, media.Channel and media.Playlist objects whose
                .source is None
            - media.Video objects whose parent is not a media.Folder (i.e.
                whose parent is a media.Channel or a media.Playlist)
            - media.Video objects in any restricted folder
            - media.Video objects in the fixed 'Unsorted Videos' folder which
                are already marked as downloaded
            - media.Video objects which have an ancestor (e.g. a parent
                media.Channel) for which checking/downloading is disabled
            - media.Video objects whose parent is a media.Folder, and whose
                file IVs are set, and for which a thumbnail exists, if
                mainapp.TartubeApp.operation_sim_shortcut_flag is set, and if
                the operation_type is 'sim'
            - media.Channel and media.Playlist objects for which checking/
                downloading are disabled, or which have an ancestor (e.g. a
                parent media.folder) for which checking/downloading is disabled
            - media.Channel, media.Playlist and media.Folder objects whose
                .dl_no_db_flag is set, during simulated downloads
            - media.Channel and media.Playlist objects during custom downloads
                in which videos are to be downloaded independently
            - media.Channel and media.Playlist objects which are disabled
                because their external directory is not available
            - media.Video objects whose parent channel/playlist/folder is
                marked unavailable because its external directory is not
                accessible
            - media.Folder objects

        Adds the resulting downloads.DownloadItem object to this object's IVs.

        Args:

            media_data_obj (media.Video, media.Channel, media.Playlist,
                media.Folder): A media data object

            scheduled_obj (media.Scheduled): The scheduled download object
                which wants to download media_data_obj (None if no scheduled
                download applies in this case)

            override_operation_type (str): After the download operation has
                started, any code can call this function to add new
                downloads.DownloadItem objects to this downloads.DownloadList,
                specifying a value that overrides the default value of
                self.operation_type. Note that this is not allowed when
                self.operation_type is 'classic_real', 'classic_sim' or
                'classic_custom', and will cause an error. The value is always
                None when called by self.__init__(). Otherwise, the value can
                be None, 'sim', 'real', 'custom_sim' or 'custom_real'

            priority_flag (bool): True if media_data_obj is to be added to the
                beginning of the list, False if it is to be added to the end
                of the list

            ignore_limits_flag (bool): True if operation limits
                (mainapp.TartubeApp.operation_limit_flag) should be ignored

            recursion_flag (bool): True when called by this function
                recursively, False when called (for the first time) by anything
                else. If False and media_data_obj is a media.Video object, we
                download it even if its parent is a channel or a playlist

        Return values:

            A list of downloads.DownloadItem objects created (an empty list if
                none are created)

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 2592 create_item')

        # (Use two lists for code clarity)
        return_list = []
        empty_list = []

        # Sanity check - if no URL is specified, then there is nothing to
        #   download
        if not isinstance(media_data_obj, media.Folder) \
        and media_data_obj.source is None:
            return empty_list

        # Apply the operation_type override, if specified
        if override_operation_type is not None:

            if self.operation_classic_flag:

                GObject.timeout_add(
                    0,
                    self.app_obj.system_error,
                    302,
                    'Invalid argument in Classic Mode tab download operation',
                )

                return empty_list

            else:

                operation_type = override_operation_type

        else:

            operation_type = self.operation_type

        if operation_type == 'custom_real' \
        or operation_type == 'classic_custom':
            custom_flag = True
        else:
            custom_flag = False

        # Get the options.OptionsManager object that applies to this media
        #   data object
        # (The manager might be specified by obj itself, or it might be
        #   specified by obj's parent, or we might use the default
        #   options.OptionsManager)
        if not self.operation_classic_flag:

            options_manager_obj = ttutils.get_options_manager(
                self.app_obj,
                media_data_obj,
            )

        else:

            # Classic Mode tab
            if self.app_obj.classic_options_obj is not None:
                options_manager_obj = self.app_obj.classic_options_obj
            else:
                options_manager_obj = self.app_obj.general_options_obj

        # Ignore private folders, and don't download any of their children
        #   (because they are all children of some other non-private folder)
        if isinstance(media_data_obj, media.Folder) \
        and media_data_obj.priv_flag:
            return empty_list

        # Don't download videos that we already have (but do check a video
        #   that's already been downloaded)
        # Don't download videos if they're in a channel or playlist (since
        #   downloading the channel/playlist downloads the videos it contains)
        # (Exception: download a single video if that's what the calling code
        #   has specifically requested)
        # (Exception: for custom downloads, do get videos independently of
        #   their channel/playlist, if allowed)
        # Don't download videos in a folder, if this is a simulated download,
        #   and the video has already been checked (exception: if the video
        #   has been passed to the download operation directly, for example by
        #   right-clicking the video and selecting 'Check video')
        # (Exception: do download videos in a folder if they're marked as
        #   livestreams, in case the livestream has finished)
        # During custom downloads that required a subtitled video, don't
        #   download an un-subtitles video
        if isinstance(media_data_obj, media.Video):

            if media_data_obj.dl_flag \
            and operation_type != 'sim' \
            and not media_data_obj.dbid \
            in self.app_obj.temp_stamp_buffer_dict \
            and not media_data_obj.dbid in self.app_obj.temp_slice_buffer_dict:
                return empty_list

            if (
                not isinstance(media_data_obj.parent_obj, media.Folder) \
                and recursion_flag
                and (
                    not custom_flag
                    or (
                        self.custom_dl_obj \
                        and not self.custom_dl_obj.dl_by_video_flag
                    ) or media_data_obj.dl_flag
                )
            ):
                return empty_list

            if isinstance(media_data_obj.parent_obj, media.Folder) \
            and (
                operation_type == 'sim' \
                or operation_type == 'custom_sim' \
                or operation_type == 'classic_sim'
            ) and self.app_obj.operation_sim_shortcut_flag \
            and recursion_flag \
            and media_data_obj.file_name \
            and not media_data_obj.live_mode \
            and ttutils.find_thumbnail(self.app_obj, media_data_obj):
                return empty_list

            if custom_flag \
            and self.custom_dl_obj \
            and self.custom_dl_obj.dl_by_video_flag:

                if self.custom_dl_obj.dl_precede_flag \
                and self.custom_dl_obj.dl_if_subs_flag \
                and (
                    not media_data_obj.subs_list \
                    or (
                        self.custom_dl_obj.dl_if_subs_list \
                        and not ttutils.match_subs(
                            self.custom_dl_obj,
                            media_data_obj.subs_list,
                        )
                    )
                ):
                    return empty_list

                elif (
                    self.custom_dl_obj.ignore_stream_flag \
                    and media_data_obj.live_mode
                ) or (
                    self.custom_dl_obj.ignore_old_stream_flag \
                    and media_data_obj.was_live_flag
                ) or (
                    self.custom_dl_obj.dl_if_stream_flag \
                    and not media_data_obj.live_mode
                ) or (
                    self.custom_dl_obj.dl_if_old_stream_flag \
                    and not media_data_obj.was_live_flag
                ):
                    return empty_list

        # Don't download videos in channels/playlists/folders which have been
        #   marked unavailable, because their external directory is not
        #   accessible
        if isinstance(media_data_obj, media.Video):
            if media_data_obj.parent_obj.dbid \
            in self.app_obj.container_unavailable_dict:
                return empty_list

        elif not isinstance(media_data_obj, media.Video) \
        and media_data_obj.dbid in self.app_obj.container_unavailable_dict:
            return empty_list

        # Don't simulated downloads of video in channels/playlists/folders
        #   whose whose .dl_no_db_flag is set
        if (operation_type == 'sim' or operation_type == 'custom_sim') \
        and (
            (
                isinstance(media_data_obj, media.Video) \
                and media_data_obj.parent_obj.dl_no_db_flag
            ) or (
                not isinstance(media_data_obj, media.Video) \
                and media_data_obj.dl_no_db_flag
            )
        ):
            return empty_list

        # Don't create a download.DownloadItem object if checking/download is
        #   disabled for the media data object
        if not isinstance(media_data_obj, media.Video) \
        and media_data_obj.dl_disable_flag:
            return empty_list

        # Don't create a download.DownloadItem object for a media.Folder,
        #   obviously
        # Don't create a download.DownloadItem object for a media.Channel or
        #   media.Playlist during a custom download in which videos are to be
        #   downloaded independently
        if (
            isinstance(media_data_obj, media.Video)
            and custom_flag
            and (
                (self.custom_dl_obj and self.custom_dl_obj.dl_by_video_flag) \
                or media_data_obj.dbid in self.app_obj.temp_stamp_buffer_dict \
                or media_data_obj.dbid in self.app_obj.temp_slice_buffer_dict
            )
        ) or (
            isinstance(media_data_obj, media.Video)
            and (
                not custom_flag \
                or (
                    self.custom_dl_obj \
                    and not self.custom_dl_obj.dl_by_video_flag
                )
            )
        ) or (
            (
                isinstance(media_data_obj, media.Channel) \
                or isinstance(media_data_obj, media.Playlist)
            ) and (
                not custom_flag \
                or (
                    self.custom_dl_obj \
                    and not self.custom_dl_obj.dl_by_video_flag
                )
            )
        ):
            # (Broadcasting livestreams should always take priority over
            #   everything else)
            if isinstance(media_data_obj, media.Video) \
            and media_data_obj.live_mode == 2:

                broadcast_flag = True
                # For a broadcasting livestream, we create additional workers
                #   if required, possibly bypassing the limit specified by
                #   mainapp.TartubeApp.num_worker_default
                if self.app_obj.download_manager_obj:
                    self.app_obj.download_manager_obj.create_bypass_worker()

            else:

                broadcast_flag = False

            # Create a new download.DownloadItem object...
            self.download_item_count += 1
            download_item_obj = DownloadItem(
                self.download_item_count,
                media_data_obj,
                scheduled_obj,
                options_manager_obj,
                operation_type,
                ignore_limits_flag,
            )

            # ...and add it to our lists
            return_list.append(download_item_obj)

            if broadcast_flag:
                self.download_item_list.insert(0, download_item_obj.item_id)
            elif priority_flag:
                self.temp_item_list.append(download_item_obj.item_id)
            else:
                self.download_item_list.append(download_item_obj.item_id)

            self.download_item_dict[download_item_obj.item_id] \
            = download_item_obj

            # Keep track of any media.Scheduled objects involved in the
            #   current download operation
            if scheduled_obj is not None \
            and not scheduled_obj in self.scheduled_list:
                self.scheduled_list.append(scheduled_obj)

        # Call this function recursively for any child media data objects in
        #   the following situations:
        #   1. A media.Folder object has children
        #   2. A media.Channel/media.Playlist object has child media.Video
        #       objects, and this is a custom download in which videos are to
        #       be downloaded independently of their channel/playlist
        if isinstance(media_data_obj, media.Folder) \
        or (
            not isinstance(media_data_obj, media.Video)
            and custom_flag
            and self.custom_dl_obj
            and self.custom_dl_obj.dl_by_video_flag
        ):
            for child_obj in media_data_obj.child_list:
                return_list += self.create_item(
                    child_obj,
                    scheduled_obj,
                    operation_type,
                    priority_flag,
                    ignore_limits_flag,
                    True,                   # Recursion
                )

        # Procedure complete
        return return_list


    def create_dummy_item(self, media_data_obj):

        """Called by self.__init__() only, when the download operation was
        launched from the Classic Mode tab (this function is not called
        recursively).

        Creates a downloads.DownloadItem object for each dummy media.Video
        object.

        Adds the resulting downloads.DownloadItem object to this object's IVs.

        Args:

            media_data_obj (media.Video): A media data object

        Return values:

            The downloads.DownloadItem object created

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 2896 create_dummy_item')

        if media_data_obj.options_obj is not None:
            # (Download options specified by the Drag and Drop tab)
            options_manager_obj = media_data_obj.options_obj
        elif self.app_obj.classic_options_obj is not None:
            options_manager_obj = self.app_obj.classic_options_obj
        else:
            options_manager_obj = self.app_obj.general_options_obj

        # Create a new download.DownloadItem object...
        self.download_item_count += 1
        download_item_obj = DownloadItem(
            media_data_obj.dbid,
            media_data_obj,
            None,                       # media.Scheduled object
            options_manager_obj,
            self.operation_type,        # 'classic_real'. 'classic_sim' or
                                        #   'classic_custom'
            False,                      # ignore_limits_flag
        )

        # ...and add it to our list
        self.download_item_list.append(download_item_obj.item_id)
        self.download_item_dict[download_item_obj.item_id] = download_item_obj

        # Procedure complete
        return download_item_obj


    @synchronise(_SYNC_LOCK)
    def fetch_next_item(self):

        """Called by downloads.DownloadManager.run().

        Based on DownloadList.fetch_next().

        Return values:

            The next downloads.DownloadItem object, or None if there are none
                left

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 2941 fetch_next_item')

        if not self.prevent_fetch_flag:

            # In case of any recent calls to self.create_item(), which want to
            #   place new DownloadItems at the beginning of the queue, then
            #   merge the temporary queue into the main one
            if self.temp_item_list:
                self.download_item_list \
                = self.temp_item_list + self.download_item_list

            for item_id in self.download_item_list:
                this_item = self.download_item_dict[item_id]

                # Don't return an item that's marked as
                #   formats.MAIN_STAGE_ACTIVE
                if this_item.stage == formats.MAIN_STAGE_QUEUED:
                    return this_item

        return None


    @synchronise(_SYNC_LOCK)
    def is_queuing(self, item_id):

        """Called by mainwin.MainWin.progress_list_popup_menu(), etc.

        Checks whether the specified DownloadItem object is waiting in the
        queue (i.e. waiting to start checking/downloading).

        Args:

            item_id (int): The .item_id of a downloads.DownloadItem object;
                should be a key in self.download_item_dict

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 2979 is_queuing')

        if item_id in self.download_item_dict:
            item_obj = self.download_item_dict[item_id]
            if item_obj.stage == formats.MAIN_STAGE_QUEUED:
                return True

        return False


    @synchronise(_SYNC_LOCK)
    def move_item_to_bottom(self, download_item_obj):

        """Called by mainwin.MainWin.on_progress_list_dl_last().

        Moves the specified DownloadItem object to the end of
        self.download_item_list, so it is assigned a DownloadWorker last
        (after all other DownloadItems).

        Args:

            download_item_obj (downloads.DownloadItem): The download item
                object to move

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 3006 move_item_to_bottom')

        # Move the item to the bottom (end) of the list
        if download_item_obj is None \
        or not download_item_obj.item_id in self.download_item_list:
            return
        else:
            self.download_item_list.append(
                self.download_item_list.pop(
                    self.download_item_list.index(download_item_obj.item_id),
                ),
            )


    @synchronise(_SYNC_LOCK)
    def move_item_to_top(self, download_item_obj):

        """Called by mainwin.MainWin.on_progress_list_dl_next().

        Moves the specified DownloadItem object to the start of
        self.download_item_list, so it is the next item to be assigned a
        DownloadWorker.

        Args:

            download_item_obj (downloads.DownloadItem): The download item
                object to move

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 3037 move_item_to_top')

        # Move the item to the top (beginning) of the list
        if download_item_obj is None \
        or not download_item_obj.item_id in self.download_item_list:
            return
        else:
            self.download_item_list.insert(
                0,
                self.download_item_list.pop(
                    self.download_item_list.index(download_item_obj.item_id),
                ),
            )


    @synchronise(_SYNC_LOCK)
    def prevent_fetch_new_items(self):

        """Called by DownloadManager.stop_download_operation_soon().

        Sets the flag that prevents calls to self.fetch_next_item() from
        fetching anything new, which allows the download operation to stop as
        soon as any ongoing video downloads have finished.
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 3063 prevent_fetch_new_items')

        self.prevent_fetch_flag = True


    @synchronise(_SYNC_LOCK)
    def set_final_item(self, item_id):

        """Called by mainwin.MainWin.on_progress_list_stop_soon(), etc.

        After the specified DownloadItem object is assigned to a worker, no
        more DownloadItem objects are assigned to a worker (i.e. do not start
        to check/download).
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 3079 set_final_item')

        if item_id in self.download_item_dict:
            self.final_item_id = item_id

        else:
            GObject.timeout_add(
                0,
                app_obj.system_error,
                318,
                _('Unrecognised download item ID'),
            )


    def reorder_master_slave(self):

        """Called by self.__init__() after the calls to self.create_item() are
        finished.

        Some media data objects have an alternate download destination, for
        example, a playlist ('slave') might download its videos into the
        directory used by a channel ('master').

        This can increase the length of the operation, because a 'slave' won't
        start until its 'master' is finished.

        Make sure all designated 'masters' are handled before 'slaves' (a media
        media data object can't be both a master and a slave).

        Even if this doesn't reduce the time the 'slaves' spend waiting to
        start, it at least makes the download order predictable.
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 3113 reorder_master_slave')

        master_list = []
        other_list = []
        for item_id in self.download_item_list:
            download_item_obj = self.download_item_dict[item_id]

            if isinstance(download_item_obj.media_data_obj, media.Video) \
            or not download_item_obj.media_data_obj.slave_dbid_list:
                other_list.append(item_id)
            else:
                master_list.append(item_id)

        self.download_item_list = []
        self.download_item_list.extend(master_list)
        self.download_item_list.extend(other_list)


class DownloadItem(object):

    """Called by downloads.DownloadList.create_item() and
    .create_dummy_item().

    Based on the DownloadItem class in youtube-dl-gui.

    Python class used to track the download status of a media data object
    (media.Video, media.Channel, media.Playlist or media.Folder), one of many
    in a downloads.DownloadList object.

    Args:

        item_id (int): The number of downloads.DownloadItem objects created,
            used to give each one a unique ID

        media_data_obj (media.Video, media.Channel, media.Playlist,
            media.Folder): The media data object to be downloaded. When the
            download operation was launched from the Classic Mode tab, a dummy
            media.Video object

        scheduled_obj (media.Scheduled): The scheduled download object which
            wants to download media_data_obj (None if no scheduled download
            applies in this case)

        options_manager_obj (options.OptionsManager): The object which
            specifies download options for the media data object

        operation_type (str): The value that applies to this DownloadItem only
            (might be different from the default value stored in
            DownloadManager.operation_type)

        ignore_limits_flag (bool): Flag set to True if operation limits
            (mainapp.TartubeApp.operation_limit_flag) should be ignored

    """


    # Standard class methods


    def __init__(self, item_id, media_data_obj, scheduled_obj,
    options_manager_obj, operation_type, ignore_limits_flag):

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 3176 __init__')

        # IV list - class objects
        # -----------------------
        # The media data object to be downloaded. When the download operation
        #   was launched from the Classic Mode tab, a dummy media.Video object
        self.media_data_obj = media_data_obj
        # The scheduled download object which wants to download media_data_obj
        #   (None if no scheduled download applies in this case)
        self.scheduled_obj = scheduled_obj
        # The object which specifies download options for the media data object
        self.options_manager_obj = options_manager_obj

        # IV list - other
        # ---------------
        # A unique ID for this object
        self.item_id = item_id
        # The current download stage
        self.stage = formats.MAIN_STAGE_QUEUED

        # The value that applies to this DownloadItem only (might be different
        #   from the default value stored in DownloadManager.operation_type)
        self.operation_type = operation_type
        # Shortcut flag to test the operation type; True for 'classic_sim',
        #   'classic_real' and 'classic_custom'; False for all other values
        self.operation_classic_flag = False         # (Set below)

        # Flag set to True if operation limits
        #   (mainapp.TartubeApp.operation_limit_flag) should be ignored
        self.ignore_limits_flag = ignore_limits_flag


        # Code
        # ----

        # Set the flag
        if operation_type == 'classic_sim' \
        or operation_type == 'classic_real' \
        or operation_type == 'classic_custom':
            self.operation_classic_flag = True


    # Set accessors


    def set_ignore_limits_flag(self):

        """Called by DownloadManager.apply_ignore_limits(), following a call
        from mainapp>TartubeApp.script_slow_timer_callback()."""

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 3227 set_ignore_limits_flag')

        self.ignore_limits_flag = True


class VideoDownloader(object):

    """Called by downloads.DownloadWorker.run_video_downloader() or
    .run_stream_downloader().

    Based on the YoutubeDLDownloader class in youtube-dl-gui.

    Python class to create a system child process. Uses the child process to
    instruct youtube-dl to download all videos associated with the URL
    described by a downloads.DownloadItem object (which might be an individual
    video, or a channel or playlist).

    Reads from the child process STDOUT and STDERR, having set up a
    downloads.PipeReader object to do so in an asynchronous way.

    Sets self.return_code to a value in the range 0-5, described below. The
    parent downloads.DownloadWorker object checks that return code once this
    object's child process has finished.

    Args:

        download_manager_obj (downloads.DownloadManager): The download manager
            object handling the entire download operation

        download_worker_obj (downloads.DownloadWorker): The parent download
            worker object. The download manager uses multiple workers to
            implement simultaneous downloads. The download manager checks for
            free workers and, when it finds one, assigns it a
            download.DownloadItem object. When the worker is assigned a
            download item, it creates a new instance of this object to
            interface with youtube-dl, and waits for this object to return a
            return code

        download_item_obj (downloads.DownloadItem): The download item object
            describing the URL from which youtube-dl should download video(s)

        force_sim_flag (bool): Set to True when called by
            .run_stream_downloader(), in which case a simulated download rather
            than a real download is performed, regardless of other settings

    Warnings:

        The calling function is responsible for calling the close() method
        when it's finished with this object, in order for this object to
        properly close down.

    """


    # Attributes


    # Valid values for self.return_code. The larger the number, the higher in
    #   the hierarchy of return codes.
    # Codes lower in the hierarchy (with a smaller number) cannot overwrite
    #   higher in the hierarchy (with a bigger number)
    #
    # 0 - The download operation completed successfully
    OK = 0
    # 1 - A warning occured during the download operation
    WARNING = 1
    # 2 - An error occured during the download operation
    ERROR = 2
    # 3 - The corresponding url video file was larger or smaller from the given
    #   filesize limit
    FILESIZE_ABORT = 3
    # 4 - The video(s) for the specified URL have already been downloaded
    ALREADY = 4
    # 5 - The download operation was stopped by the user
    STOPPED = 5
    # 6 - The download operation has stalled. The parent worker can restart it,
    #   if required
    STALLED = -1


    # Standard class methods


    def __init__(self, download_manager_obj, download_worker_obj, \
    download_item_obj, force_sim_flag=False):

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 3314 __init__')

        # IV list - class objects
        # -----------------------
        # The downloads.DownloadManager object handling the entire download
        #   operation
        self.download_manager_obj = download_manager_obj
        # The parent downloads.DownloadWorker object
        self.download_worker_obj = download_worker_obj
        # The downloads.DownloadItem object describing the URL from which
        #   youtube-dl should download video(s)
        self.download_item_obj = download_item_obj

        # The child process created by self.create_child_process()
        self.child_process = None

        # Read from the child process STDOUT (i.e. self.child_process.stdout)
        #   and STDERR (i.e. self.child_process.stderr) in an asynchronous way
        #   by polling this queue.PriorityQueue object
        self.queue = queue.PriorityQueue()
        self.stdout_reader = PipeReader(self.queue, 'stdout')
        self.stderr_reader = PipeReader(self.queue, 'stderr')


        # IV list - other
        # ---------------
        # The current return code, using values in the range 0-5, as described
        #   above
        # The value remains set to self.OK unless we encounter any problems
        # The larger the number, the higher in the hierarchy of return codes.
        #   Codes lower in the hierarchy (with a smaller number) cannot
        #   overwrite higher in the hierarchy (with a bigger number)
        self.return_code = self.OK
        # The time (in seconds) between iterations of the loop in
        #   self.do_download()
        self.sleep_time = 0.1
        # The time (in seconds) to wait for an existing download, which shares
        #   a common download destination with this media data object, to
        #   finish downloading
        self.long_sleep_time = 10

        # The time (matches time.time() ) at which the first youtube-dl
        #   network error was detected. Reset back to None when the download
        #   resumes. If the download does not resume quickly enough
        #   (according to settings), then this download is marked as stalled,
        #   and can be restarted, if settings require that
        self.network_error_time = None

        # Flag set to True if we are simulating downloads for this media data
        #   object, or False if we actually downloading videos (updated below)
        self.dl_sim_flag = force_sim_flag
        # Flag set to True if this download operation was launched from the
        #   Classic Mode tab, False if not (set below)
        self.dl_classic_flag = False

        # Flag set to True by a call from any function to self.stop_soon()
        # After being set to True, this VideoDownloader should give up after
        #   the next call to self.confirm_new_video(), .confirm_old_video()
        #   .confirm_sim_video()
        self.stop_soon_flag = False
        # Exception: after the FFmpeg "Merging formats into..." message, wait
        #   for the merge to complete before giving up
        self.stop_after_merge_flag = False
        # When self.stop_soon_flag is True, the next call to
        #   self.confirm_new_video(), .confirm_old_video() or
        #   .confirm_sim_video() sets this flag to True, informing
        #   self.do_download() that it can stop the child process
        self.stop_now_flag = False

        # youtube-dl is passed a URL, which might represent an individual
        #   video, a channel or a playlist
        # Assume it's an individual video unless youtube-dl reports a
        #   channel or playlist (in which case, we can update these IVs later)
        # For real downloads, self.video_num is the current video number, and
        #   self.video_total is the number of videos in the channel/playlist
        # For simulated downloads, both IVs are set to the number of
        #   videos actually found
        self.video_num = 0
        self.video_total = 0
        # When the 'Downloading webpage' message is detected, denoting the
        #   start of a real (not simulated) download, this IV is set to the
        #   video's ID. The value is reset when self.confirm_new_video() etc
        #   is called, or when an error/warning with a different video ID is
        #   detected
        # When set, any youtube-dl errors/warnings which do not specify their
        #   own video ID can be assumed to belong to this video
        self.probable_video_id = None
        # self.extract_stdout_data() detects the completion of a download job
        #   in one of several ways
        # The first time it happens for each individual video,
        #   self.extract_stdout_data() takes action. It calls
        #   self.confirm_new_video(), self.confirm_old_video() or
        #   self.confirm_sim_video() when required
        # On subsequent occasions, the completion message is ignored (as
        #   youtube-dl may pass us more than one completion message for a
        #   single video)
        # There is one exception: in calls to self.confirm_new_video, a
        #   subsequent call to self.confirm_new_video() updates the file
        #   extension of the media.Video. (yt-dlp and/or FFmpeg may send
        #   several completion messages as it converts one file format to
        #   another; the final one is the one we want)
        # Dictionary of videos, used to check for the first completion message
        #   for each unique video
        # Dictionary in the form
        #       key = the video number (matches self.video_num)
        #       value = the media.Video object created
        self.video_check_dict = {}
        # The code imported from youtube-dl-gui doesn't recognise a downloaded
        #   video, if FFmpeg isn't used to extract it (because FFmpeg is not
        #   installed, or because the website doesn't support it, or whatever)
        # In this situation, youtube-dl's STDOUT messages don't definitively
        #   establish when it has finished downloading a video
        # When a file destination is announced; it is temporarily stored in
        #   these IVs. When STDOUT receives a message in the form
        #       [download] 100% of 2.06MiB in 00:02
        #   ...and the filename isn't one that FFmpeg would use (e.g.
        #       'myvideo.f136.mp4' or 'myvideo.f136.m4a', then assume that the
        #       video has finished downloading
        self.temp_path = None
        self.temp_filename = None
        self.temp_extension = None

        # When checking a channel/playlist, this number is incremented every
        #   time youtube-dl gives us the details of a video which the Tartube
        #   database already contains (with a minimum number of IVs already
        #   set)
        # When downloading a channel/playlist, this number is incremented every
        #   time youtube-dl gives us a 'video already downloaded' message
        #   (unless the Tartube database hasn't actually marked the video as
        #   downloaded)
        # Every time the value is incremented, we check the limits specified by
        #   mainapp.TartubeApp.operation_check_limit or
        #   .operation_download_limit. If the limit has been reached, we stop
        #   checking/downloading the channel/playlist
        # No check is carried out if self.download_item_obj represents an
        #   individual media.Video object (and not a whole channel or playlist)
        self.video_limit_count = 0
        # Git issue #9 describes youtube-dl failing to download the video's
        #   JSON metadata. We can't do anything about the youtube-dl code, but
        #   we can apply our own timeout
        # This IV is set whenever self.confirm_sim_video() is called. After
        #   being set, if a certain time has passed without another call to
        #   self.confirm_sim_video, self.do_download() halts the child process
        # The time to wait is specified by mainapp.TartubeApp IVs
        #   .json_timeout_no_comments_time and .json_timeout_with_comments_time
        self.last_sim_video_check_time = None

        # If mainapp.TartubeApp.operation_convert_mode is set to any value
        #   other than 'disable', then a media.Video object whose URL
        #   represents a channel/playlist is converted into multiple new
        #   media.Video objects, one for each video actually downloaded
        # Flag set to True when self.download_item_obj.media_data_obj is a
        #   media.Video object, but a channel/playlist is detected (regardless
        #   of the value of mainapp.TartubeApp.operation_convert_mode)
        self.url_is_not_video_flag = False
        # Flag which specifies whether formats.ACTIVE_STAGE_PRE_PROCESS or
        #   formats.ACTIVE_STAGE_POST_PROCESS currently applies
        # Set to True by self.extract_stdout_data() when
        #   formats.ACTIVE_STAGE_DOWNLOAD is detected; set back to False by the
        #   same function when the start of a new video download is detected
        self.video_download_started_flag = False

        # Buffer for youtube-dl error/warning messages that can be associated
        #   with a particular video ID
        # The corresponding media.Video object might not exist at the time the
        #   error/warning is processed, so it is temporarily stored here, so
        #   that the parent downloads.DownloadWorker can retrieve it
        # Dictionary in the form
        #   key = The video ID (corresponds to media.Video.vid)
        #   value = A list in the form
        #       [ [type, message], [type, message] ... ]
        # ...where 'type' is the string 'error' or 'warning', and 'message'
        #   is the error/warning generated
        self.video_msg_buffer_dict = {}
        # Errors/warnings for individual media.Video objects requires special
        #   handling. We can't predict where, in the check/download process,
        #   the first error/warning will occur
        # Dictionary of videos which have been assigned an error/warning
        #   by this instance of the VideoDownloader. The first error/warning
        #   removes any errors/warnings generated by previous operations.
        #   The call to self.confirm_new_video(), .confirm_old_video() and
        #   .confirm_sim_video() removes any errors/warnings generated by
        #   previous operations by consulting this dictionary
        # Dictionary in the form
        #   key = The video ID (corresponds to media.Video.vid)
        #   value = True (not required)
        self.video_error_warning_dict = {}

        # List of regexes used by self.extract_stdout_data() to check for
        #   certain filtered videos
        # As of January 2025, these regexes match both youtube-dl and yt-dlp
        self.filter_regex_list = [
            r'upload date is not in range',
            r'because it has not reached minimum view count',
            r'because it has exceeded the maximum view count',
            r'because it is age restricted',
        ]

        # For channels/playlists, a list of child media.Video objects, used to
        #   track missing videos (when required)
        self.missing_video_check_list = []
        # Flag set to True (for convenience) if the list is populated
        self.missing_video_check_flag = False


        # Code
        # ----
        # Initialise IVs depending on whether this is a real or simulated
        #   download
        media_data_obj = self.download_item_obj.media_data_obj

        # All media data objects can be marked as simulate downloads only
        #   (except when the download operation was launched from the Classic
        #   Mode tab)
        # The setting applies not just to the media data object, but all of its
        #   descendants
        if not self.download_item_obj.operation_classic_flag:

            if (
                force_sim_flag \
                or self.download_item_obj.operation_type == 'sim' \
                or self.download_item_obj.operation_type == 'custom_sim'
            ):
                dl_sim_flag = True
            else:
                dl_sim_flag = media_data_obj.dl_sim_flag
                parent_obj = media_data_obj.parent_obj

                while not dl_sim_flag and parent_obj is not None:
                    dl_sim_flag = parent_obj.dl_sim_flag
                    parent_obj = parent_obj.parent_obj

            if dl_sim_flag:
                self.dl_sim_flag = True
            else:
                self.dl_sim_flag = False

        else:

            self.dl_classic_flag = True
            if self.download_item_obj.operation_type == 'classic_sim':
                self.dl_sim_flag = True

        # If the user wants to detect missing videos in channels/playlists
        #   (those that have been downloaded by the user, but since removed
        #   from the website by the creator), set that up
        if (
            isinstance(media_data_obj, media.Channel) \
            or isinstance(media_data_obj, media.Playlist)
        ) and (
            self.download_item_obj.operation_type == 'real' \
            or self.download_item_obj.operation_type == 'sim'
        ) and download_manager_obj.app_obj.track_missing_videos_flag:

            # Compile a list of child videos. Videos can be removed from the
            #   list as they are detected
            self.missing_video_check_list = media_data_obj.child_list.copy()
            if self.missing_video_check_list:
                self.missing_video_check_flag = True


    # Public class methods


    def do_download(self):

        """Called by downloads.DownloadWorker.run_video_downloader().

        Based on YoutubeDLDownloader.download().

        Downloads video(s) from a URL described by self.download_item_obj.

        Return values:

            The final return code, a value in the range 0-5 (as described
                above)

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 3578 do_download')

        # Import the main application (for convenience)
        app_obj = self.download_manager_obj.app_obj

        # Set the default return code. Everything is OK unless we encounter
        #   any problems
        self.set_return_code(self.OK)

        if not self.dl_classic_flag:

            # Reset the errors/warnings stored in the media data object, the
            #   last time it was checked/downloaded
            self.download_item_obj.media_data_obj.reset_error_warning()
            if isinstance(
                self.download_item_obj.media_data_obj,
                media.Video,
            ):
                self.download_item_obj.media_data_obj.set_block_flag(False)

            else:
                # If two channels/playlists/folders share a download
                #   destination, we don't want to download both of them at the
                #   same time
                # If this media data obj shares a download destination with
                #   another downloads.DownloadWorker, wait until that download
                #   has finished before starting this one
                while self.download_manager_obj.check_master_slave(
                    self.download_item_obj.media_data_obj,
                ):
                    time.sleep(self.long_sleep_time)

        # Prepare a system command...
        options_obj = self.download_worker_obj.options_manager_obj
        if options_obj.options_dict['direct_cmd_flag']:

            cmd_list = ttutils.generate_direct_system_cmd(
                app_obj,
                self.download_item_obj.media_data_obj,
                options_obj,
            )

        else:

            divert_mode = None
            if (
                self.download_item_obj.operation_type == 'custom_real' \
                or self.download_item_obj.operation_type == 'classic_custom'
            ) and isinstance(
                self.download_item_obj.media_data_obj,
                media.Video,
            ) and self.download_manager_obj.custom_dl_obj:
                divert_mode \
                = self.download_manager_obj.custom_dl_obj.divert_mode

            cmd_list = ttutils.generate_ytdl_system_cmd(
                app_obj,
                self.download_item_obj.media_data_obj,
                self.download_worker_obj.options_list,
                self.dl_sim_flag,
                self.dl_classic_flag,
                self.missing_video_check_flag,
                self.download_manager_obj.custom_dl_obj,
                divert_mode,
            )

        # ...display it in the Output tab (if required)...
        display_cmd = ttutils.prepare_system_cmd_for_display(cmd_list)
        if app_obj.ytdl_output_system_cmd_flag:
            app_obj.main_win_obj.output_tab_write_system_cmd(
                self.download_worker_obj.worker_id,
                display_cmd,
            )

        # ...and the terminal (if required)
        if app_obj.ytdl_write_system_cmd_flag:
            print(display_cmd)

        # ...and the downloader log (if required)
        if app_obj.ytdl_log_system_cmd_flag:
            app_obj.write_downloader_log(display_cmd)

        # Create a new child process using that command...
        self.create_child_process(cmd_list)
        # ...and set up the PipeReader objects to read from the child process
        #   STDOUT and STDERR
        if self.child_process is not None:
            self.stdout_reader.attach_fh(self.child_process.stdout)
            self.stderr_reader.attach_fh(self.child_process.stderr)

        # While downloading the media data object, update the callback function
        #   with the status of the current job
        while self.is_child_process_alive():

            # Pause a moment between each iteration of the loop (we don't want
            #   to hog system resources)
            time.sleep(self.sleep_time)

            # Read from the child process STDOUT and STDERR, in the correct
            #   order, until there is nothing left to read
            while self.read_child_process():
                pass

            # Apply the JSON timeout, if required
            if app_obj.apply_json_timeout_flag \
            and self.last_sim_video_check_time is not None \
            and self.last_sim_video_check_time < time.time():
                # Halt the child process, which stops checking this channel/
                #   playlist
                self.stop()

                GObject.timeout_add(
                    0,
                    app_obj.system_error,
                    303,
                    'Enforced timeout because downloader took too long to' \
                    + ' fetch a video\'s JSON data',
                )

            # If a download has stalled (there has been no activity for some
            #   time), halt the child process (allowing the parent worker to
            #   restart the stalled download, if required)
            if app_obj.operation_auto_restart_flag \
            and self.network_error_time is not None:

                restart_time = app_obj.operation_auto_restart_time * 60
                if (self.network_error_time + restart_time) < time.time():

                    # Stalled download. Stop the child process
                    self.stop()

                    # Pass a dictionary of values to downloads.DownloadWorker,
                    #   confirming the result of the job. The values are passed
                    #   on to the main window
                    self.set_return_code(self.STALLED)
                    self.last_data_callback()

                    return self.return_code

            # Stop this video downloader, if required to do so, having just
            #   finished checking/downloading a video
            if self.stop_now_flag:
                self.stop()

        # The child process has finished
        # We also set the return code to self.ERROR if the download didn't
        #   start or if the child process return code is greater than 0
        # Original notes from youtube-dl-gui:
        #   NOTE: In Linux if the called script is just empty Python exits
        #       normally (ret=0), so we can't detect this or similar cases
        #       using the code below
        #   NOTE: In Unix a negative return code (-N) indicates that the child
        #       was terminated by signal N (e.g. -9 = SIGKILL)
        internal_msg = None
        if self.child_process is None:
            self.set_return_code(self.ERROR)
            internal_msg = _('Download did not start')

        elif self.child_process.returncode > 0:
            self.set_return_code(self.ERROR)
            if not app_obj.ignore_child_process_exit_flag:
                internal_msg = _(
                    'Child process exited with non-zero code: {}',
                ).format(self.child_process.returncode)

        if internal_msg:

            # (The message must be visible in the Errors/Warnings tab, the
            #   Output tab, terminal and/or downloader log)
            self.set_error(
                self.download_item_obj.media_data_obj,
                internal_msg,
            )

            if app_obj.ytdl_output_stderr_flag:
                app_obj.main_win_obj.output_tab_write_stderr(
                    self.download_worker_obj.worker_id,
                    internal_msg,
                )

            if app_obj.ytdl_write_stderr_flag:
                print(internal_msg)

            if app_obj.ytdl_log_stderr_flag:
                app_obj.write_downloader_log(internal_msg)

        # For channels/playlists, detect missing videos (those downloaded by
        #   the user, but since deleted from the website by the creator)
        # We only perform the check if the process completed without errors,
        #   and was not halted early by the user (or halted by the download
        #   manager, because too many videos have been downloaded)
        # We also ignore livestreams
        detected_list = []

        if app_obj.track_missing_videos_flag \
        and self.missing_video_check_list \
        and self.download_manager_obj.running_flag \
        and not self.stop_soon_flag \
        and not self.stop_now_flag \
        and self.return_code <= self.WARNING \
        and self.video_num > 0:
            for check_obj in self.missing_video_check_list:
                if check_obj.dbid in app_obj.media_reg_dict \
                and check_obj.dl_flag \
                and not check_obj.live_mode:

                    # Filter out videos that are too old
                    if (
                        app_obj.track_missing_time_flag \
                        and app_obj.track_missing_time_days > 0
                    ):
                        # Convert the video's upload time from seconds to days
                        days = check_obj.upload_time / (60 * 60 * 24)
                        if days <= app_obj.track_missing_time_days:

                            # Mark this video as missing
                            detected_list.append(check_obj)

                    else:

                        # Mark this video as missing
                        detected_list.append(check_obj)

        for detected_obj in detected_list:
            app_obj.mark_video_missing(
                detected_obj,
                True,       # Video is missing
                True,       # Don't update the Video Index
                True,       # Don't update the Video Catalogue
                True,       # Don't sort the parent channel/playlist
            )

        # Pass a dictionary of values to downloads.DownloadWorker, confirming
        #   the result of the job. The values are passed on to the main
        #   window
        self.last_data_callback()

        # Pass the result back to the parent downloads.DownloadWorker object
        return self.return_code


    def check_dl_is_correct_type(self):

        """Called by self.extract_stdout_data().

        When youtube-dl reports the URL associated with the download item
        object contains multiple videos (or potentially contains multiple
        videos), then the URL represents a channel or playlist, not a video.

        This function checks whether a channel/playlist is about to be
        downloaded into a media.Video object. If so, it takes action to prevent
        that from happening.

        The action taken depends on the value of
        mainapp.TartubeApp.operation_convert_mode.

        Return values:

            False if a channel/playlist was about to be downloaded into a
                media.Video object, which has since been replaced by a new
                media.Channel/media.Playlist object

            True in all other situations (including when a channel/playlist was
                about to be downloaded into a media.Video object, which was
                not replaced by a new media.Channel/media.Playlist object)

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 3847 check_dl_is_correct_type')

        # Special case: if the download operation was launched from the
        #   Classic Mode tab, there is no need to do anything
        if self.dl_classic_flag:
            return True

        # Otherwise, import IVs (for convenience)
        app_obj = self.download_manager_obj.app_obj
        media_data_obj = self.download_item_obj.media_data_obj

        if isinstance(self.download_item_obj.media_data_obj, media.Video):

            # If the mode is 'disable', or if it the original media.Video
            #   object is contained in a channel or a playlist, then we must
            #   stop downloading this URL immediately
            if app_obj.operation_convert_mode == 'disable' \
            or not isinstance(
                self.download_item_obj.media_data_obj.parent_obj,
                media.Folder,
            ):
                self.url_is_not_video_flag = True

                # Stop downloading this URL
                self.stop()
                self.set_error(
                    media_data_obj,
                    '\'' + media_data_obj.name + '\' ' + _(
                        'This video has a URL that points to a channel or a' \
                        + ' playlist, not a video',
                    ),
                )

                # Don't allow self.confirm_sim_video() to be called
                return False

            # Otherwise, we can create new media.Video objects for each
            #   video downloaded/checked. The new objects may be placd into a
            #   new media.Channel or media.Playlist object
            elif not self.url_is_not_video_flag:

                self.url_is_not_video_flag = True

                # Mark the original media.Video object to be destroyed at the
                #   end of the download operation
                self.download_manager_obj.mark_video_as_doomed(media_data_obj)

                if app_obj.operation_convert_mode != 'multi':

                    # Create a new media.Channel or media.Playlist object and
                    #   add it to the download manager
                    # Then halt this job, so the new channel/playlist object
                    #   can be downloaded
                    self.convert_video_to_container()

                # Don't allow self.confirm_sim_video() to be called
                return False

        # Do allow self.confirm_sim_video() to be called
        return True


    def close(self):

        """Can be called by anything.

        Destructor function for this object.
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 3917 close')

        # Tell the PipeReader objects to shut down, thus joining their threads
        self.stdout_reader.join()
        self.stderr_reader.join()


    def confirm_archived_video(self, filename):

        """Called by self.extract_stdout_data().

        A modified version of self.confirm_old_video(), called when
        youtube-dl's 'has already been recorded in archive' message is detected
        (but only when checking for missing videos).

        Tries to find a match for the video name and, if one is found, marks it
        as not missing.

        Args:

            filename (str): The video name, which should match the .name of a
                media.Video object in self.missing_video_check_list

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 3943 confirm_archived_video')

        # Create shortcut variables (for convenience)
        app_obj = self.download_manager_obj.app_obj
        media_data_obj = self.download_item_obj.media_data_obj

        # media_data_obj is a media.Channel or media.Playlist object. Check its
        #   child objects, looking for a matching video
        match_obj = media_data_obj.find_matching_video(app_obj, filename)
        if match_obj and match_obj in self.missing_video_check_list:
            self.missing_video_check_list.remove(match_obj)


    def confirm_filtered_video(self):

        """Called by self.extract_stdout_data().

        A modified version of self.confirm_old_video(), handling only the
        checks for operation limits.

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 3944 confirm_filtered_video')

        # Create shortcut variables (for convenience)
        app_obj = self.download_manager_obj.app_obj

        # This filtered video applies towards the limit specified by
        #  mainapp.TartubeApp.operation_download_limit (which the calling code
        #   has already checked is enabled)

        self.video_limit_count += 1

        if not isinstance(self.download_item_obj.media_data_obj, media.Video) \
        and not self.download_item_obj.ignore_limits_flag:

            if (
                self.dl_sim_flag \
                and app_obj.operation_check_limit \
                and self.video_limit_count >= app_obj.operation_check_limit
            ) or (
                not self.dl_sim_flag \
                and app_obj.operation_download_limit \
                and self.video_limit_count >= app_obj.operation_download_limit
            ):
                # Limit reached; stop downloading videos in this channel/
                #   playlist
                self.stop()


    def confirm_new_video(self, dir_path, filename, extension, \
    merge_flag=False):

        """Called by self.extract_stdout_data().

        A successful download is announced in one of several ways.

        When an announcement is detected, this function is called. Use the
        first announcement to update self.video_check_dict. For subsequent
        announcements, only a media.Video's file extension is updated (see the
        comments in self.__init__() ).

        Args:

            dir_path (str): The full path to the directory in which the video
                is saved, e.g. '/home/yourname/tartube/downloads/Videos'

            filename (str): The video's filename, e.g. 'My Video'

            extension (str): The video's extension, e.g. '.mp4'

            merge_flag (bool): True if this function was called as the result
                of a 'Merging formats into...' message

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 3983 confirm_new_video')

        # Create shortcut variables (for convenience)
        app_obj = self.download_manager_obj.app_obj
        media_data_obj = self.download_item_obj.media_data_obj

        # Error/warning handling for individual videos
        video_obj = None

        # Special case: don't add videos to the Tartube database at all
        if not isinstance(media_data_obj, media.Video) \
        and media_data_obj.dl_no_db_flag:

            # Add this video to the buffer that will handle the removal of
            #   metadata files, at the end of the download operation
            app_obj.other_metadata_buffer_list.append({
                'options_obj': self.download_worker_obj.options_manager_obj,
                'dir_path': dir_path,
                'filename': filename,
            })

            # Register the download with DownloadManager, so that download
            #   limits can be applied, if required
            self.download_manager_obj.register_video('new')

        # Special case: if the download operation was launched from the
        #   Classic Mode tab, then we only need to update the dummy
        #   media.Video object, and to move/remove description/metadata/
        #   thumbnail files, as appropriate
        elif self.dl_classic_flag:

            self.confirm_new_video_classic_mode(dir_path, filename, extension)

        # All other cases
        elif not self.video_num in self.video_check_dict:

            # Create a new media.Video object for the video
            if self.url_is_not_video_flag:

                video_obj = app_obj.convert_video_from_download(
                    self.download_item_obj.media_data_obj.parent_obj,
                    self.download_item_obj.options_manager_obj,
                    dir_path,
                    filename,
                    extension,
                    True,               # Don't sort parent containers yet
                )

            else:

                video_obj = app_obj.create_video_from_download(
                    self.download_item_obj,
                    dir_path,
                    filename,
                    extension,
                    True,               # Don't sort parent containers yet
                )

            # If downloading from a channel/playlist, remember the video's
            #   index. (The server supplies an index even for a channel, and
            #   the user might want to convert a channel to a playlist)
            if self.video_num > 0 and (
                isinstance(video_obj.parent_obj, media.Channel) \
                or isinstance(video_obj.parent_obj, media.Playlist)
            ):
                video_obj.set_index(self.video_num)

            # Contact SponsorBlock server to fetch video slice data
            if app_obj.custom_sblock_mirror != '' \
            and app_obj.sblock_fetch_flag \
            and video_obj.vid != None \
            and (not video_obj.slice_list or app_obj.sblock_replace_flag):
                ttutils.fetch_slice_data(
                    app_obj,
                    video_obj,
                    self.download_worker_obj.worker_id,
                    True,       # Write to terminal/log, if allowed
                )

            # Update the main window
            GObject.timeout_add(
                0,
                app_obj.announce_video_download,
                self.download_item_obj,
                video_obj,
                ttutils.compile_mini_options_dict(
                    self.download_worker_obj.options_manager_obj,
                ),
            )

            # Register the download with DownloadManager, so that download
            #   limits can be applied, if required
            self.download_manager_obj.register_video('new')

            # Update the checklist
            if self.video_num > 0:
                self.video_check_dict[self.video_num] = video_obj

        elif self.video_num > 0:

            # Update the video's file extension, in case one file format has
            #   been converted to another (with a new call to this function
            #   each time)
            video_obj = self.video_check_dict[self.video_num]

            if video_obj.file_ext is None \
            or (extension is not None and video_obj.file_ext != extension):
                video_obj.set_file_ext(extension)

        # The probable video ID, if captured, can now be reset
        self.probable_video_id = None

        if video_obj:

            # If no errors/warnings were received during this operation,
            #   errors/warnings that already exist (from previous operations)
            #   can now be cleared
            if not video_obj.dbid in self.video_error_warning_dict:
                video_obj.reset_error_warning()

            # This confirmation clears a video marked as blocked
            video_obj.set_block_flag(False)

        # This VideoDownloader can now stop, if required to do so after a video
        #   has been checked/downloaded
        if self.stop_soon_flag:
            if merge_flag and not self.stop_now_flag:
                self.stop_after_merge_flag = True
            else:
                self.stop_now_flag = True


    def confirm_new_video_classic_mode(self, dir_path, filename, extension):

        """Called by self.confirm_new_video() when a download operation was
        launched from the Classic Mode tab.

        Handles the download.

        Args:

            dir_path (str): The full path to the directory in which the video
                is saved, e.g. '/home/yourname/tartube/downloads/Videos'

            filename (str): The video's filename, e.g. 'My Video'

            extension (str): The video's extension, e.g. '.mp4'

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 4135 confirm_new_video_classic_mode')

        # Import the main application (for convenience)
        app_obj = self.download_manager_obj.app_obj

        # Update the dummy media.Video object
        dummy_obj = self.download_item_obj.media_data_obj

        dummy_obj.set_dl_flag(True)
        dummy_obj.set_dummy_path(
            os.path.abspath(os.path.join(dir_path, filename + extension)),
        )

        # Contact SponsorBlock server to fetch video slice data
        if app_obj.custom_sblock_mirror != '' \
        and app_obj.sblock_fetch_flag \
        and dummy_obj.vid != None \
        and (not dummy_obj.slice_list or app_obj.sblock_replace_flag):
            ttutils.fetch_slice_data(
                app_obj,
                dummy_obj,
                self.download_worker_obj.worker_id,
                True,       # Write to terminal/log, if allowed
            )

        # Add this video to the buffer that will handle the removal of metadata
        #   files, at the end of the download operation
        app_obj.other_metadata_buffer_list.append({
            'options_obj': self.download_worker_obj.options_manager_obj,
            'dir_path': dir_path,
            'filename': filename,
            'dummy_obj': dummy_obj,
        })

        # Register the download with DownloadManager, so that download limits
        #   can be applied, if required
        self.download_manager_obj.register_video('new')

        # The probable video ID, if captured, can now be reset
        self.probable_video_id = None


    def confirm_old_video(self, dir_path, filename, extension):

        """Called by self.extract_stdout_data().

        When youtube-dl reports a video has already been downloaded, make sure
        the media.Video object is marked as downloaded, and upate the main
        window if necessary.

        Args:

            dir_path (str): The full path to the directory in which the video
                is saved, e.g. '/home/yourname/tartube/downloads/Videos'

            filename (str): The video's filename, e.g. 'My Video'

            extension (str): The video's extension, e.g. '.mp4'

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 4197 confirm_old_video')

        # Create shortcut variables (for convenience)
        app_obj = self.download_manager_obj.app_obj
        media_data_obj = self.download_item_obj.media_data_obj

        # Error/warning handling for individual videos
        if isinstance(media_data_obj, media.Video):
            video_obj = media_data_obj
        else:
            video_obj = None

        # Special case: don't add videos to the Tartube database at all
        if video_obj is None and media_data_obj.dl_no_db_flag:

            # Register the download with DownloadManager, so that download
            #   limits can be applied, if required
            self.download_manager_obj.register_video('old')

        # Special case: if the download operation was launched from the
        #   Classic Mode tab, then we only need to update the dummy
        #   media.Video object
        elif self.dl_classic_flag:

            media_data_obj.set_dl_flag(True)
            media_data_obj.set_dummy_path(
                os.path.abspath(os.path.join(dir_path, filename + extension)),
            )

            # Register the download with DownloadManager, so that download
            #   limits can be applied, if required
            self.download_manager_obj.register_video('old')

        # All other cases
        elif video_obj:

            # v2.4.456: added an additional check; if youtube-dl downloaded the
            #   video but Tartube's database didn't detect it in the filesystem
            #   (for example because of encoding problems in Git #320), then
            #   this call to mark_video_downloaded() messes up the database
            if not video_obj.dl_flag \
            and video_obj.name == filename \
            and os.path.isfile(
                os.path.abspath(os.path.join(dir_path, filename + extension)),
            ):
                GObject.timeout_add(
                    0,
                    app_obj.mark_video_downloaded,
                    video_obj,
                    True,               # Video is downloaded
                    True,               # Video is not new
                )

        else:

            # media_data_obj is a media.Channel or media.Playlist object. Check
            #   its child objects, looking for a matching video
            match_obj = media_data_obj.find_matching_video(app_obj, filename)
            if match_obj:

                # This video will not be marked as a missing video
                if match_obj in self.missing_video_check_list:
                    self.missing_video_check_list.remove(match_obj)

                if not match_obj.dl_flag:

                    GObject.timeout_add(
                        0,
                        app_obj.mark_video_downloaded,
                        match_obj,
                        True,           # Video is downloaded
                        True,           # Video is not new
                    )

                else:

                    # Register the download with DownloadManager, so that
                    #   download limits can be applied, if required
                    self.download_manager_obj.register_video('old')

                    # This video applies towards the limit (if any) specified
                    #   by mainapp.TartubeApp.operation_download_limit
                    self.video_limit_count += 1

                    if not isinstance(
                        self.download_item_obj.media_data_obj,
                        media.Video,
                    ) \
                    and not self.download_item_obj.ignore_limits_flag \
                    and app_obj.operation_limit_flag \
                    and app_obj.operation_download_limit \
                    and self.video_limit_count >= \
                    app_obj.operation_download_limit:
                        # Limit reached; stop downloading videos in this
                        #   channel/playlist
                        self.stop()

            else:

                # No match found, so create a new media.Video object for the
                #   video file that already exists on the user's filesystem
                video_obj = app_obj.create_video_from_download(
                    self.download_item_obj,
                    dir_path,
                    filename,
                    extension,
                )

                if self.video_num > 0:
                    self.video_check_dict[self.video_num] = video_obj

                # Update the main window
                if media_data_obj.external_dir is not None \
                and media_data_obj.master_dbid != media_data_obj.dbid:

                    # The container is storing its videos in another
                    #   container's sub-directory, which (probably) explains
                    #   why we couldn't find a match. Don't add anything to the
                    #   Results List
                    GObject.timeout_add(
                        0,
                        app_obj.announce_video_clone,
                        video_obj,
                    )

                else:

                    # Do add an entry to the Results List (as well as updating
                    #   the Video Catalogue, as normal)
                    GObject.timeout_add(
                        0,
                        app_obj.announce_video_download,
                        self.download_item_obj,
                        video_obj,
                        ttutils.compile_mini_options_dict(
                            self.download_worker_obj.options_manager_obj,
                        ),
                    )

                    # Register the download with DownloadManager, so that
                    #   download limits can be applied, if required
                    self.download_manager_obj.register_video('new')

        # The probable video ID, if captured, can now be reset
        self.probable_video_id = None

        if video_obj:

            # If no errors/warnings were received during this operation,
            #   errors/warnings that already exist (from previous operations)
            #   can now be cleared
            if not video_obj.dbid in self.video_error_warning_dict:
                video_obj.reset_error_warning()

            # This confirmation clears a video marked as blocked
            video_obj.set_block_flag(False)

        # This VideoDownloader can now stop, if required to do so after a video
        #   has been checked/downloaded
        if self.stop_soon_flag:
            self.stop_now_flag = True


    def confirm_remuxed_video(self, dir_path, filename, extension):

        """Called by self.extract_stdout_data().

        Written to handle problems described in Git #714.

        When youtube-dl reports a video has been remuxed, make sure that the
        media.Video object has its file extension updated.

        If no matching video can be found, call .confirm_old_video() to handle
        it.

        Args:

            dir_path (str): The full path to the directory in which the video
                is saved, e.g. '/home/yourname/tartube/downloads/Videos'

            filename (str): The video's filename, e.g. 'My Video'

            extension (str): The video's extension, e.g. '.mp4'

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 4197 confirm_remuxed_video')

        # Create shortcut variables (for convenience)
        app_obj = self.download_manager_obj.app_obj
        media_data_obj = self.download_item_obj.media_data_obj

        # Find the matching video, and update its file extension
        if isinstance(media_data_obj, media.Video):
            video_obj = media_data_obj

        else:
            video_obj = media_data_obj.find_matching_video(app_obj, filename)

        if video_obj:
            video_obj.set_file_ext(extension)

        else:
            # No matching video found, so let .confirm_old_video() handle it
            return confirm_old_video(self, dir_path, filename, extension)


    def confirm_sim_video(self, json_dict):

        """Called by self.extract_stdout_data().

        After a successful simulated download, youtube-dl presents us with JSON
        data for the video. Use that data to update everything.

        Args:

            json_dict (dict): JSON data from STDOUT, converted into a python
                dictionary

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 4368 confirm_sim_video')

        # Create shortcut variables (for convenience)
        app_obj = self.download_manager_obj.app_obj
        dl_list_obj = self.download_manager_obj.download_list_obj
        options_obj = self.download_worker_obj.options_manager_obj
        # Call self.stop(), if the limit described in the comments for
        #   self.__init__() have been reached
        stop_flag = False

        # Set the time at which a JSON timeout should be applied, if no more
        #   calls to this function have been made
        if app_obj.apply_json_timeout_flag:

            if (
                self.dl_sim_flag \
                and options_obj.options_dict['check_fetch_comments']
            ) or (
                not self.dl_sim_flag \
                and options_obj.options_dict['dl_fetch_comments']
            ):
                wait_secs = app_obj.json_timeout_with_comments_time * 60
            else:
                wait_secs = app_obj.json_timeout_no_comments_time * 60

            self.last_sim_video_check_time = int(time.time()) + wait_secs

        # From the JSON dictionary, extract the data we need
        # Git #177 reports that this value might be 'None', so check for that
        if '_filename' in json_dict \
        and json_dict['_filename'] is not None:
            full_path = json_dict['_filename']
            path, filename, extension = self.extract_filename(full_path)
        else:
            GObject.timeout_add(
                0,
                app_obj.system_error,
                304,
                'Missing filename in JSON data',
            )

            return

        # (Git #322, 'upload_date' might be None)
        if 'upload_date' in json_dict \
        and json_dict['upload_date'] is not None:

            try:
                # date_string in form YYYYMMDD
                date_string = json_dict['upload_date']
                dt_obj = datetime.datetime.strptime(date_string, '%Y%m%d')
                upload_time = dt_obj.timestamp()
            except:
                upload_time = None

        else:
            upload_time = None

        if 'duration' in json_dict:
            duration = json_dict['duration']
        else:
            duration = None

        if 'title' in json_dict:
            name = json_dict['title']
        else:
            name = None

        if 'id' in json_dict:
            vid = json_dict['id']

        chapter_list = []
        if 'chapters' in json_dict:
            chapter_list = json_dict['chapters']

        if 'description' in json_dict:
            descrip = json_dict['description']
        else:
            descrip = None

        if 'thumbnail' in json_dict:
            thumbnail = json_dict['thumbnail']
        else:
            thumbnail = None

#        if 'webpage_url' in json_dict:
#            source = json_dict['webpage_url']
#        else:
#            source = None
        # !!! DEBUG: yt-dlp Git #119: filter out the extraneous characters at
        #   the end of the URL, if present
        if 'webpage_url' in json_dict:

            source = re.sub(
                r'\&has_verified\=.*\&bpctr\=.*',
                '',
                json_dict['webpage_url'],
            )

        else:
            source = None

        if 'playlist_index' in json_dict:
            playlist_index = json_dict['playlist_index']
        else:
            playlist_index = None

        if 'is_live' in json_dict:
            if json_dict['is_live']:
                live_flag = True
            else:
                live_flag = False
        else:
            live_flag = False

        if 'was_live' in json_dict:
            if json_dict['was_live']:
                was_live_flag = True
            else:
                was_live_flag = False
        else:
            was_live_flag = False

        if 'comments' in json_dict:
            comment_list = json_dict['comments']
        else:
            comment_list = []

        if 'playlist_id' in json_dict:
            playlist_id = json_dict['playlist_id']
            if 'playlist_title' in json_dict:
                playlist_title = json_dict['playlist_title']
            else:
                playlist_title = None
        else:
            playlist_id = None

        if 'subtitles' in json_dict and json_dict['subtitles']:
            subs_flag = True
        else:
            subs_flag = False

        # Does an existing media.Video object match this video?
        media_data_obj = self.download_item_obj.media_data_obj
        video_obj = None

        if self.url_is_not_video_flag:

            # media_data_obj has a URL which represents a channel or playlist,
            #   but media_data_obj itself is a media.Video object
            # media_data_obj's parent is a media.Folder object. Check its
            #   child objects, looking for a matching video
            # (video_obj is set to None, if no match is found)
            video_obj = media_data_obj.parent_obj.find_matching_video(
                app_obj,
                filename,
            )

            if not video_obj:
                video_obj = media_data_obj.parent_obj.find_matching_video(
                    app_obj,
                    name,
                )

        elif isinstance(media_data_obj, media.Video):

            # media_data_obj is a media.Video object
            video_obj = media_data_obj

        else:

            # media_data_obj is a media.Channel or media.Playlist object. Check
            #   its child objects, looking for a matching video
            # (video_obj is set to None, if no match is found)
            video_obj = media_data_obj.find_matching_video(app_obj, filename)
            if not video_obj:
                video_obj = media_data_obj.find_matching_video(app_obj, name)

        new_flag = False
        update_results_flag = False
        if not video_obj:

            # Special case: during the checking phase of a custom download,
            #   don't create a new media.Video object if the video has no
            #   available subtitles (if that's what the settings in the
            #   CustomDLManager specify)
            if (
                self.download_item_obj.operation_type == 'custom_sim' \
                or self.download_item_obj.operation_type == 'classic_sim'
            ) and dl_list_obj.custom_dl_obj \
            and dl_list_obj.custom_dl_obj.dl_by_video_flag \
            and dl_list_obj.custom_dl_obj.dl_precede_flag \
            and dl_list_obj.custom_dl_obj.dl_if_subs_flag \
            and dl_list_obj.custom_dl_obj.ignore_if_no_subs_flag \
            and (
                not subs_flag \
                or (
                    dl_list_obj.custom_dl_obj.dl_if_subs_list \
                    and not ttutils.match_subs(
                        dl_list_obj.custom_dl_obj,
                        list(json_dict['subtitles'].keys),
                    )
                )
            ):
                return

            # No matching media.Video object found, so create a new one
            new_flag = True
            update_results_flag = True

            if self.url_is_not_video_flag:

                video_obj = app_obj.convert_video_from_download(
                    self.download_item_obj.media_data_obj.parent_obj,
                    self.download_item_obj.options_manager_obj,
                    path,
                    filename,
                    extension,
                    # Don't sort parent container objects yet; wait for
                    #   mainwin.MainWin.results_list_update_row() to do it
                    True,
                )

            else:

                video_obj = app_obj.create_video_from_download(
                    self.download_item_obj,
                    path,
                    filename,
                    extension,
                    True,
                )

            # Update its IVs with the JSON information we extracted
            if filename is not None:
                video_obj.set_name(filename)

            if name is not None:
                video_obj.set_nickname(name)
            elif filename is not None:
                video_obj.set_nickname(filename)

            if vid is not None:
                video_obj.set_vid(vid)

            if upload_time is not None:
                video_obj.set_upload_time(upload_time)

            if duration is not None:
                video_obj.set_duration(duration)

            if source is not None:
                video_obj.set_source(source)

            if chapter_list:
                video_obj.extract_timestamps_from_chapters(
                    app_obj,
                    chapter_list,
                )

            if descrip is not None:
                video_obj.set_video_descrip(
                    app_obj,
                    descrip,
                    app_obj.main_win_obj.descrip_line_max_len,
                )

            if was_live_flag:
                video_obj.set_was_live_flag(True)

            if comment_list \
            and options_obj.options_dict['store_comments_in_db']:
                video_obj.set_comments(comment_list)

            if app_obj.store_playlist_id_flag \
            and playlist_id is not None \
            and not isinstance(video_obj.parent_obj, media.Folder):
                video_obj.parent_obj.set_playlist_id(
                    playlist_id,
                    playlist_title,
                )

            if subs_flag:
                video_obj.extract_subs_list(json_dict['subtitles'])

            app_obj.extract_parent_name_from_metadata(
                video_obj,
                json_dict,
            )

            if isinstance(video_obj.parent_obj, media.Channel) \
            or isinstance(video_obj.parent_obj, media.Playlist):
                # 'Enhanced' websites only: set the channel/playlist RSS feed,
                #   if not already set
                video_obj.parent_obj.update_rss_from_json(json_dict)

                # If downloading from a channel/playlist, remember the video's
                #   index. (The server supplies an index even for a channel,
                #   and the user might want to convert a channel to a playlist)
                video_obj.set_index(playlist_index)

            # Now we can sort the parent containers
            video_obj.parent_obj.sort_children(app_obj)
            app_obj.fixed_all_folder.sort_children(app_obj)
            if video_obj.bookmark_flag:
                app_obj.fixed_bookmark_folder.sort_children(app_obj)
            if video_obj.fav_flag:
                app_obj.fixed_fav_folder.sort_children(app_obj)
            if video_obj.live_mode:
                app_obj.fixed_live_folder.sort_children(app_obj)
            if video_obj.missing_flag:
                app_obj.fixed_missing_folder.sort_children(app_obj)
            if video_obj.new_flag:
                app_obj.fixed_new_folder.sort_children(app_obj)
            if video_obj in app_obj.fixed_recent_folder.child_list:
                app_obj.fixed_recent_folder.sort_children(app_obj)
            if video_obj.waiting_flag:
                app_obj.fixed_waiting_folder.sort_children(app_obj)

        else:

            # This video will not be marked as a missing video
            if video_obj in self.missing_video_check_list:
                self.missing_video_check_list.remove(video_obj)

            # A media.Video object that already exists is not displayed in the
            #   Results list (unless it's a downloaded video that is being
            #   re-checked)
            if video_obj.file_name \
            and video_obj.name != app_obj.default_video_name \
            and not video_obj.dl_flag:

                # This video must not be displayed in the Results List, and
                #   counts towards the limit (if any) specified by
                #   mainapp.TartubeApp.operation_check_limit
                self.video_limit_count += 1

                if not isinstance(
                    self.download_item_obj.media_data_obj,
                    media.Video,
                ) \
                and not self.download_item_obj.ignore_limits_flag \
                and app_obj.operation_limit_flag \
                and app_obj.operation_check_limit \
                and self.video_limit_count >= app_obj.operation_check_limit:
                    # Limit reached. When we reach the end of this function,
                    #   stop checking videos in this channel/playlist
                    stop_flag = True

                # The call to DownloadManager.register_video() below doesn't
                #   take account of this situation, so make our own call
                self.download_manager_obj.register_video('other')

            else:

                # This video must be displayed in the Results List, and counts
                #   towards the limit (if any) specified by
                #   mainapp.TartubeApp.autostop_videos_value
                update_results_flag = True

            # If the 'Add videos' button was used, the path/filename/extension
            #   won't be set yet
            if not video_obj.file_name and full_path:
                video_obj.set_file(filename, extension)

            # Update any video object IVs that are not set
            if video_obj.name == app_obj.default_video_name \
            and filename is not None:
                video_obj.set_name(filename)

            if video_obj.nickname == app_obj.default_video_name:
                if name is not None:
                    video_obj.set_nickname(name)
                elif filename is not None:
                    video_obj.set_nickname(filename)

            if not video_obj.vid and vid is not None:
                video_obj.set_vid(vid)

            if not video_obj.upload_time and upload_time is not None:
               video_obj.set_upload_time(upload_time)

            if not video_obj.duration and duration is not None:
                video_obj.set_duration(duration)

            if not video_obj.source and source is not None:
                video_obj.set_source(source)

            if chapter_list:
                video_obj.extract_timestamps_from_chapters(
                    app_obj,
                    chapter_list,
                )

            if not video_obj.descrip and descrip is not None:
                video_obj.set_video_descrip(
                    app_obj,
                    descrip,
                    app_obj.main_win_obj.descrip_line_max_len,
                )

            if was_live_flag:
                video_obj.set_was_live_flag(True)

            if not video_obj.comment_list \
            and comment_list \
            and options_obj.options_dict['store_comments_in_db']:
                video_obj.set_comments(comment_list)

            if app_obj.store_playlist_id_flag \
            and playlist_id is not None \
            and not isinstance(video_obj.parent_obj, media.Folder):
                video_obj.parent_obj.set_playlist_id(
                    playlist_id,
                    playlist_title,
                )

            if subs_flag:
                video_obj.extract_subs_list(json_dict['subtitles'])

            app_obj.extract_parent_name_from_metadata(
                video_obj,
                json_dict,
            )

            if isinstance(video_obj.parent_obj, media.Channel) \
            or isinstance(video_obj.parent_obj, media.Playlist):
                # 'Enhanced' websites only: set the channel/playlist RSS feed,
                #   if not already set
                video_obj.parent_obj.update_rss_from_json(json_dict)

                # If downloading from a channel/playlist, remember the video's
                #   index. (The server supplies an index even for a channel,
                #   and the user might want to convert a channel to a playlist)
                video_obj.set_index(playlist_index)

        # Deal with livestreams
        if video_obj.live_mode != 2 and live_flag:

            GObject.timeout_add(
                0,
                app_obj.mark_video_live,
                video_obj,
                2,                  # Livestream is broadcasting
                {},                 # No livestream data
                True,               # Don't update Video Index yet
                True,               # Don't update Video Catalogue yet
            )

        elif video_obj.live_mode != 0 and not live_flag:

            GObject.timeout_add(
                0,
                app_obj.mark_video_live,
                video_obj,
                0,                  # Livestream has finished
                {},                 # Reset any livestream data
                True,               # Don't update Video Index yet
                True,               # Don't update Video Catalogue yet
            )

        # Deal with the video description, JSON data and thumbnail, according
        #   to the settings in options.OptionsManager
        options_dict \
        = self.download_worker_obj.options_manager_obj.options_dict

        if descrip and options_dict['write_description']:

            descrip_path = os.path.abspath(
                os.path.join(path, filename + '.description'),
            )

            if not options_dict['sim_keep_description']:

                descrip_path = ttutils.convert_path_to_temp_dl_dir(
                    app_obj,
                    descrip_path,
                )

            # (Don't replace a file that already exists, and obviously don't
            #   do anything if the call returned None because of a filesystem
            #   error)
            if descrip_path is not None and not os.path.isfile(descrip_path):

                try:
                    fh = open(descrip_path, 'wb')
                    fh.write(descrip.encode('utf-8'))
                    fh.close()

                    if options_dict['move_description']:
                        ttutils.move_metadata_to_subdir(
                            app_obj,
                            video_obj,
                            '.description',
                        )

                except:
                    pass

        if options_dict['write_info']:

            json_path = os.path.abspath(
                os.path.join(path, filename + '.info.json'),
            )

            if not options_dict['sim_keep_info']:
                json_path = ttutils.convert_path_to_temp_dl_dir(
                    app_obj,
                    json_path,
                )

            if json_path is not None and not os.path.isfile(json_path):

                try:
                    with open(json_path, 'w') as outfile:
                        json.dump(json_dict, outfile, indent=4)

                    if options_dict['move_info']:
                        ttutils.move_metadata_to_subdir(
                            app_obj,
                            video_obj,
                            '.info.json',
                        )

                except:
                    pass

        # v2.1.101 - Annotations were removed by YouTube in 2019, so this
        #   feature is not available, and will not be available until the
        #   authors have some annotations to test
#        if options_dict['write_annotations']:
#
#            xml_path = os.path.abspath(
#                os.path.join(path, filename + '.annotations.xml'),
#            )
#
#            if not options_dict['sim_keep_annotations']:
#                xml_path \
#                = ttutils.convert_path_to_temp_dl_dir(app_obj, xml_path)

        if thumbnail and options_dict['write_thumbnail']:

            # Download the thumbnail, if we don't already have it
            # The thumbnail's URL is something like
            #   'https://i.ytimg.com/vi/abcdefgh/maxresdefault.jpg'
            # When saved to disc by youtube-dl, the file is given the same name
            #   as the video (but with a different extension)
            # Get the thumbnail's extension...
            remote_file, remote_ext = os.path.splitext(thumbnail)
            # Fix for Odysee videos, whose thumbnail extension is not specified
            #   in the .info.json file
            if remote_ext == '':
                remote_ext = '.webp'

            # ...and thus get the filename used by youtube-dl when storing the
            #   thumbnail locally
            thumb_path = video_obj.get_actual_path_by_ext(app_obj, remote_ext)

            if not options_dict['sim_keep_thumbnail']:
                thumb_path = ttutils.convert_path_to_temp_dl_dir(
                    app_obj,
                    thumb_path,
                )

            if thumb_path is not None and not os.path.isfile(thumb_path):

                # v2.0.013 The requests module fails if the connection drops
                # v1.2.006 Writing the file fails if the directory specified
                #   by thumb_path doesn't exist
                # Use 'try' so that neither problem is fatal
                try:
                    request_obj = requests.get(
                        thumbnail,
                        timeout = app_obj.request_get_timeout,
                    )

                    with open(thumb_path, 'wb') as outfile:
                        outfile.write(request_obj.content)

                except:
                    pass

            # Convert .webp thumbnails to .jpg, if required
            thumb_path = ttutils.find_thumbnail_webp_intact_or_broken(
                app_obj,
                video_obj,
            )
            if thumb_path is not None \
            and not app_obj.ffmpeg_fail_flag \
            and app_obj.ffmpeg_convert_webp_flag \
            and not app_obj.ffmpeg_manager_obj.convert_webp(thumb_path):

                app_obj.set_ffmpeg_fail_flag(True)
                GObject.timeout_add(
                    0,
                    app_obj.system_error,
                    305,
                    app_obj.ffmpeg_fail_msg,
                )

            # Move to the sub-directory, if required
            if options_dict['move_thumbnail']:

                ttutils.move_thumbnail_to_subdir(app_obj, video_obj)

        # Contact SponsorBlock server to fetch video slice data
        if app_obj.custom_sblock_mirror != '' \
        and app_obj.sblock_fetch_flag \
        and video_obj.vid != None \
        and (not video_obj.slice_list or app_obj.sblock_replace_flag):
            ttutils.fetch_slice_data(
                app_obj,
                video_obj,
                self.download_worker_obj.worker_id,
                True,       # Write to terminal/log, if allowed
            )

        # If a new media.Video object was created (or if a video whose name is
        #   unknown, now has a name), add a line to the Results List, as well
        #   as updating the Video Catalogue
        # The True argument passes on the download options 'move_description',
        #   etc, but not 'keep_description', etc
        if update_results_flag:

            GObject.timeout_add(
                0,
                app_obj.announce_video_download,
                self.download_item_obj,
                video_obj,
                # No call to ttutils.compile_mini_options_dict(), because this
                #   function deals with download options like
                #   'move_description' by itself
                {},
            )

        else:

            # Otherwise, just update the Video Catalogue
            GObject.timeout_add(
                0,
                app_obj.main_win_obj.video_catalogue_update_video,
                video_obj,
            )

        # For simulated downloads, self.do_download() has not displayed
        #   anything in the Output tab/terminal window/downloader log; so do
        #   that now (if required)
        if app_obj.ytdl_output_stdout_flag:

            app_obj.main_win_obj.output_tab_write_stdout(
                self.download_worker_obj.worker_id,
                '[' + video_obj.parent_obj.name + '] <' \
                + _('Simulated download of:') + ' \'' + filename + '\'>',
            )

        if app_obj.ytdl_write_stdout_flag:

            # v2.2.039 Partial fix for Git #106, #115 and #175, for which we
            #   get a Python error when print() receives unicode characters
            filename = filename.encode().decode(
                ttutils.get_encoding(),
                'replace',
            )

            try:

                print(
                    '[' + video_obj.parent_obj.name + '] <' \
                    + _('Simulated download of:') + ' \'' + filename + '\'>',
                )

            except:

                print(
                    '[' + video_obj.parent_obj.name + '] <' \
                    + _(
                    'Simulated download of video with unprintable characters',
                    ) + '>',
                )

        if app_obj.ytdl_log_stdout_flag:

            app_obj.write_downloader_log(
                '[' + video_obj.parent_obj.name + '] <' \
                + _('Simulated download of:') + ' \'' + filename + '\'>',
            )

        # If a new media.Video object was created (or if a video whose name is
        #   unknown, now has a name), register the simulated download with
        #   DownloadManager, so that download limits can be applied, if
        #   required
        if update_results_flag:
            self.download_manager_obj.register_video('sim')

        if video_obj:

            # If no errors/warnings were received during this operation,
            #   errors/warnings that already exist (from previous operations)
            #   can now be cleared
            if not video_obj.dbid in self.video_error_warning_dict:
                video_obj.reset_error_warning()

            # This confirmation clears a video marked as blocked
            video_obj.set_block_flag(False)

        # Stop checking videos in this channel/playlist, if a limit has been
        #   reached
        if stop_flag:
            self.stop()

        # This VideoDownloader can now stop, if required to do so after a video
        #   has been checked/downloaded
        elif self.stop_soon_flag:
            self.stop_now_flag = True


    def convert_video_to_container(self):

        """Called by self.check_dl_is_correct_type().

        Creates a new media.Channel or media.Playlist object to replace an
        existing media.Video object. The new object is given some of the
        properties of the old one.

        This function doesn't destroy the old object; DownloadManager.run()
        handles that.
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 5079 convert_video_to_container')

        app_obj = self.download_manager_obj.app_obj
        old_video_obj = self.download_item_obj.media_data_obj
        container_obj = old_video_obj.parent_obj

        # Some media.Folder objects cannot contain channels or playlists (for
        #   example, the 'Unsorted Videos' folder)
        # If that is the case, the new channel/playlist is created without a
        #   parent. Otherwise, it is created at the same location as the
        #   original media.Video object
        if container_obj.restrict_mode != 'open':
            container_obj = None

        # Decide on a name for the new channel/playlist, e.g. 'channel_1' or
        #   'playlist_4'. The name must not already be in use. The user can
        #   customise the name when they're ready
        name = ttutils.find_available_name(
            app_obj,
            # e.g. 'channel'
            app_obj.operation_convert_mode,
            # Allow 'channel_1', if available
            1,
        )

        # (Prevent any possibility of an infinite loop by giving up after some
        #   thousands of attempts)
        name = None
        new_container_obj = None

        for n in range (1, 9999):
            test_name = app_obj.operation_convert_mode + '_'  + str(n)
            if not app_obj.is_container(test_name):
                name = test_name
                break

        if name is not None:

            # Create the new channel/playlist. Very unlikely that the old
            #   media.Video object has its .dl_sim_flag set, but we'll use it
            #   nonetheless
            if app_obj.operation_convert_mode == 'channel':

                new_container_obj = app_obj.add_channel(
                    name,
                    container_obj,      # May be None
                    source = old_video_obj.source,
                    dl_sim_flag = old_video_obj.dl_sim_flag,
                )

            else:

                new_container_obj = app_obj.add_playlist(
                    name,
                    container_obj,      # May be None
                    source = old_video_obj.source,
                    dl_sim_flag = old_video_obj.dl_sim_flag,
                )

        if new_container_obj is None:

            # New channel/playlist could not be created (for some reason), so
            #   stop downloading from this URL
            self.stop()
            self.set_error(
                media_data_obj,
                '\'' + media_data_obj.name + '\' ' + _(
                    'This video has a URL that points to a channel or a' \
                    + ' playlist, not a video',
                ),
            )

        else:

            # Update IVs for the new channel/playlist object
            new_container_obj.set_options_obj(old_video_obj.options_obj)
            new_container_obj.set_source(old_video_obj.source)

            # Add the new channel/playlist to the Video Index (but don't
            #   select it)
            GObject.timeout_add(
                0,
                app_obj.main_win_obj.video_index_add_row,
                new_container_obj,
                True,
            )

            # Add the new channel/playlist to the download manager's list of
            #   things to download...
            return_list \
            = self.download_manager_obj.download_list_obj.create_item(
                new_container_obj,
                self.download_item_obj.scheduled_obj,
                self.download_item_obj.operation_type,
                False,                  # priority_flag
                self.download_item_obj.ignore_limits_flag,
            )

            # ...and add rows in the Progress List
            for new_download_item_obj in return_list:
                GObject.timeout_add(
                    0,
                    app_obj.main_win_obj.progress_list_add_row,
                    new_download_item_obj.item_id,
                    new_download_item_obj.media_data_obj,
                )

            # Stop this download job, allowing the replacement one to start
            self.stop()


    def create_child_process(self, cmd_list):

        """Called by self.do_download() immediately after the call to
        ttutils.generate_ytdl_system_cmd().

        Based on YoutubeDLDownloader._create_process().

        Executes the system command, creating a new child process which
        executes youtube-dl.

        Sets self.return_code in the event of an error.

        Args:

            cmd_list (list): Python list that contains the command to execute

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 5200 create_child_process')

        # Strip double quotes from arguments
        # (Since we're sending the system command one argument at a time, we
        #   don't need to retain the double quotes around any single argument
        #   and, in fact, doing so would cause an error)
        cmd_list = ttutils.strip_double_quotes(cmd_list)

        # Create the child process
        info = preexec = None

        if os.name == 'nt':
            # Hide the child process window that MS Windows helpfully creates
            #   for us
            info = subprocess.STARTUPINFO()
            info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        else:
            # Make this child process the process group leader, so that we can
            #   later kill the whole process group with os.killpg
            preexec = os.setsid

        try:
            self.child_process = subprocess.Popen(
                cmd_list,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                preexec_fn=preexec,
                startupinfo=info,
            )

        except (ValueError, OSError) as error:
            # (There is no need to update the media data object's error list,
            #   as the code in self.do_download() will notice the child
            #   process didn't start, and set its own error message)
            self.set_return_code(self.ERROR)


    def extract_filename(self, input_data):

        """Called by self.confirm_sim_video() and .extract_stdout_data().

        Based on the extract_data() function in youtube-dl-gui's
        downloaders.py.

        Extracts various components of a filename.

        Args:

            input_data (str): Full path to a file which has been downloaded
                and saved to the filesystem

        Return values:

            Returns the path, filename and extension components of the full
                file path.

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 5259 extract_filename')

        path, fullname = os.path.split(input_data.strip("\""))
        filename, extension = os.path.splitext(fullname)

        return path, filename, extension


    def extract_stdout_data(self, stdout):

        """Called by self.read_child_process().

        Based on the extract_data() function in youtube-dl-gui's
        downloaders.py.

        Extracts youtube-dl statistics from the child process.

        Args:

            stdout (str): String that contains a line from the child process
                STDOUT (i.e., a message from youtube-dl)

        Return values:

            Python dictionary in a standard format also used by the main window
            code. Dictionaries in this format are generally called
            'dl_stat_dict' (or some variation of it).

            The returned dictionary can be empty if there is no data to
            extract, otherwise it contains one or more of the following keys:

            'status'         : Contains the status of the download
            'path'           : Destination path
            'filename'       : The filename without the extension
            'extension'      : The file extension
            'percent'        : The percentage of the video being downloaded
            'eta'            : Estimated time for the completion of the
                                download
            'speed'          : Download speed
            'filesize'       : The size of the video file being downloaded
            'playlist_index' : The playlist index of the current video file
                                being downloaded
            'playlist_size'  : The number of videos in the playlist
            'dl_sim_flag'    : Flag set to True if we are simulating downloads
                                for this media data object, or False if we
                                actually downloading videos (set below)

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 5309 extract_stdout_data')

        # Import the main application and media data object (for convenience)
        app_obj = self.download_manager_obj.app_obj
        media_data_obj = self.download_item_obj.media_data_obj

        # Initialise the dictionary with default key-value pairs for the main
        #   window to display, to be overwritten (if possible) with new key-
        #   value pairs as this function interprets the STDOUT message
        dl_stat_dict = {
            'playlist_index': self.video_num,
            'playlist_size': self.video_total,
            'dl_sim_flag': self.dl_sim_flag,
        }

        # If STDOUT has not been received by this function, then the main
        #   window can be passed just the default key-value pairs
        if not stdout:
            return dl_stat_dict

        # In some cases, we want to preserve the multiple successive whitespace
        #   characters in the STDOUT message, in order to extract filenames
        #   in their original form
        # In other cases, we just eliminate multiple successive whitespace
        #   characters
        stdout_with_spaces_list = stdout.split(' ')
        stdout_list = stdout.split()

        # The '[download] XXX has already been recorded in the archive'
        #   message does not cause a call to self.confirm_new_video(), etc,
        #   so we must handle it here
        # (Note that the first word might be '[download]', or '[Youtube]', etc)
        match = re.search(
            r'^\[\w+\]\s(.*)\shas already been recorded in (the )?' \
            + 'archive$',
            stdout,
        )
        if match:

            # In the Classic Mode tab, marking a (dummy) video as downloaded
            #   allows the 'Clear downloaded videos' button to work with it
            if self.dl_classic_flag:
                self.download_item_obj.media_data_obj.set_dl_flag(True)
                self.download_manager_obj.register_video('other')
                return dl_stat_dict

            # If checking missing videos, update our list of missing videos
            if self.missing_video_check_flag:
                self.confirm_archived_video(match.group(1))
                self.download_manager_obj.register_video('other')
                return dl_stat_dict

        # Likewise for the frame messages from youtube-dl direct downloads
        match = re.search(
            r'^frame.*size\=\s*([\S]+).*bitrate\=\s*([\S]+)',
            stdout,
        )
        if match:
            dl_stat_dict['filesize'] = match.groups()[0]
            dl_stat_dict['speed'] = match.groups()[1]
            return dl_stat_dict

        # Depending on settings, some filtered videos may count towards the
        #   operation limit. As we have to match several regexes, first check
        #   that the operation limit is enabled
        if app_obj.operation_limit_include_out_of_range_flag is True:

            for regex in self.filter_regex_list:
                match = re.search(regex, stdout)
                if match:
                    self.confirm_filtered_video()
                    return dl_stat_dict

        # Detect the start of a new channel/playlist/video download
        if stdout_list[1] == 'Extracting' and stdout_list[2] == 'URL:':
            self.video_download_started_flag = False

        # Extract the data. Because of the (small) possibility of a Python
        #   IndexError, we need to wrap the whole thing in a try..except
        try:

            stdout_list[0] = stdout_list[0].lstrip('\r')
            if stdout_list[0] == '[download]':

                dl_stat_dict['status'] = formats.ACTIVE_STAGE_DOWNLOAD
                self.video_download_started_flag = True

                if self.network_error_time is not None:
                    self.network_error_time = None

                # Get path, filename and extension
                if stdout_list[1] == 'Destination:':
                    path, filename, extension = self.extract_filename(
                        ' '.join(stdout_with_spaces_list[2:]),
                    )

                    dl_stat_dict['path'] = path
                    dl_stat_dict['filename'] = filename
                    dl_stat_dict['extension'] = extension

                    # v2.3.013 - the path to the subtitles file is being
                    #   mistaken for the path to the video file here. Only use
                    #   the destination if the path is a recognised video/audio
                    #   format (and if we don't already have it)
                    short_ext = extension[1:]
                    if self.temp_path is None \
                    and (
                        short_ext in formats.VIDEO_FORMAT_LIST \
                        or short_ext in formats.AUDIO_FORMAT_LIST
                    ):
                        self.set_temp_destination(path, filename, extension)

                # Get progress information
                if '%' in stdout_list[1]:
                    if stdout_list[1] != '100%':

                        # Old format, e.g.
                        #   [download]  27.0% of 7.55MiB at 73.63KiB/s ETA
                        #       01:16
                        if stdout_list[3] != '~':
                            dl_stat_dict['percent'] = stdout_list[1]
                            dl_stat_dict['eta'] = stdout_list[7]
                            dl_stat_dict['speed'] = stdout_list[5]
                            dl_stat_dict['filesize'] = stdout_list[3]
                        # New format (approx December 2022), e.g.
                        #   [download] 8.5% of ~ 19.87MiB at 2.35MiB/s ETA
                        #       00:07 (frag 8/94)
                        else:
                            dl_stat_dict['percent'] = stdout_list[1]
                            dl_stat_dict['eta'] = stdout_list[8]
                            dl_stat_dict['speed'] = stdout_list[6]
                            dl_stat_dict['filesize'] = stdout_list[4]

                    else:
                        dl_stat_dict['percent'] = '100%'
                        dl_stat_dict['eta'] = ''
                        dl_stat_dict['speed'] = ''
                        dl_stat_dict['filesize'] = stdout_list[3]

                        # If the most recently-received filename isn't one used
                        #   by FFmpeg, then this marks the end of a video
                        #   download
                        # (See the comments in self.__init__)
                        if len(stdout_list) > 4 \
                        and stdout_list[4] == 'in' \
                        and self.temp_filename is not None \
                        and not re.search(
                            r'^.*\.f\d{1,3}$',
                            self.temp_filename,
                        ):
                            self.confirm_new_video(
                                self.temp_path,
                                self.temp_filename,
                                self.temp_extension,
                            )

                            self.reset_temp_destination()

                # Get playlist information (when downloading a channel or a
                #   playlist, this line is received once per video)
                # youtube-dl 'Downloading video n of n'
                # yt-dlp: 'Downloading item n of n'
                if stdout_list[1] == 'Downloading' \
                and (stdout_list[2] == 'video' or stdout_list[2] == 'item') \
                and stdout_list[4] == 'of':
                    dl_stat_dict['playlist_index'] = int(stdout_list[3])
                    self.video_num = int(stdout_list[3])
                    dl_stat_dict['playlist_size'] = int(stdout_list[5])
                    self.video_total = int(stdout_list[5])

                    # If youtube-dl is about to download a channel or playlist
                    #   into a media.Video object, decide what to do to prevent
                    #   it
                    if not self.dl_classic_flag:
                        self.check_dl_is_correct_type()

                # Remove the 'and merged' part of the STDOUT message when using
                #   FFmpeg to merge the formats
                if stdout_list[-3] == 'downloaded' \
                and stdout_list[-1] == 'merged':
                    stdout_list = stdout_list[:-2]
                    stdout_with_spaces_list = stdout_with_spaces_list[:-2]

                    dl_stat_dict['percent'] = '100%'

                # Get file already downloaded status
#               if stdout_list[-1] == 'downloaded':
                if re.search(r' has already been downloaded$', stdout):

                    path, filename, extension = self.extract_filename(
                        ' '.join(stdout_with_spaces_list[1:-4]),
                    )

                    # v2.3.013 - same problem as above
                    short_ext = extension[1:]
                    if short_ext in formats.VIDEO_FORMAT_LIST \
                    or short_ext in formats.AUDIO_FORMAT_LIST:

                        dl_stat_dict['status'] \
                        = formats.COMPLETED_STAGE_ALREADY
                        dl_stat_dict['path'] = path
                        dl_stat_dict['filename'] = filename
                        dl_stat_dict['extension'] = extension
                        self.reset_temp_destination()

                        self.confirm_old_video(path, filename, extension)

                # Get filesize abort status
                if stdout_list[-1] == 'Aborting.':
                    dl_stat_dict['status'] = formats.ERROR_STAGE_ABORT

            elif stdout_list[0] == '[hlsnative]':

                # Get information from the native HLS extractor (see
                #   https://github.com/rg3/youtube-dl/blob/master/youtube_dl/
                #       downloader/hls.py#L54
                dl_stat_dict['status'] = formats.ACTIVE_STAGE_DOWNLOAD
                self.video_download_started_flag = True

                if len(stdout_list) == 7:
                    segment_no = float(stdout_list[6])
                    current_segment = float(stdout_list[4])

                    # Get the percentage
                    percent \
                    = '{0:.1f}%'.format(current_segment / segment_no * 100)
                    dl_stat_dict['percent'] = percent

            # youtube-dl uses [ffmpeg], yt-dlp uses [Merger] or [ExtractAudio]
            elif stdout_list[0] == '[ffmpeg]' \
            or stdout_list[0] == '[Merger]' \
            or stdout_list[0] == '[ExtractAudio]':

                # Using FFmpeg, not the the native HLS extractor
                # A successful video download is announced in one of several
                #   ways. Use the first announcement to update
                #   self.video_check_dict, and ignore subsequent announcements
                dl_stat_dict['status'] = formats.ACTIVE_STAGE_POST_PROCESS

                # Get the final file extension after the merging process has
                #   completed
                if stdout_list[1] == 'Merging':
                    path, filename, extension = self.extract_filename(
                        ' '.join(stdout_with_spaces_list[4:]),
                    )

                    dl_stat_dict['path'] = path
                    dl_stat_dict['filename'] = filename
                    dl_stat_dict['extension'] = extension
                    self.reset_temp_destination()

                    self.confirm_new_video(path, filename, extension, True)

                # Get the final file extension after simple FFmpeg post-
                #   processing (i.e. not after a file merge)
                elif stdout_list[1] == 'Destination:':
                    path, filename, extension = self.extract_filename(
                        ' '.join(stdout_with_spaces_list[2:]),
                    )

                    dl_stat_dict['path'] = path
                    dl_stat_dict['filename'] = filename
                    dl_stat_dict['extension'] = extension
                    self.reset_temp_destination()

                    self.confirm_new_video(path, filename, extension)

                # Get final file extension after the recoding process
                elif stdout_list[1] == 'Converting':
                    path, filename, extension = self.extract_filename(
                        ' '.join(stdout_with_spaces_list[8:]),
                    )

                    dl_stat_dict['path'] = path
                    dl_stat_dict['filename'] = filename
                    dl_stat_dict['extension'] = extension
                    self.reset_temp_destination()

                    self.confirm_new_video(path, filename, extension)

            elif stdout_list[0] == '[VideoRemuxer]':

                # Get final file extension after the remuxing process
                path, filename, extension = self.extract_filename(
                    ' '.join(stdout_with_spaces_list[8:]),
                )

                dl_stat_dict['path'] = path
                dl_stat_dict['filename'] = filename
                dl_stat_dict['extension'] = extension
                self.reset_temp_destination()

                self.confirm_remuxed_video(path, filename, extension)

            elif (
                isinstance(media_data_obj, media.Channel)
                and not media_data_obj.rss \
                and stdout_list[0] == '[youtube:channel]' \
            ) or (
                isinstance(media_data_obj, media.Playlist) \
                and not media_data_obj.rss \
                and stdout_list[0] == '[youtube:playlist]' \
                and stdout_list[2] == 'Downloading' \
                and stdout_list[3] == 'webpage'
            ):
                # YouTube only: set the channel/playlist RSS feed, if not
                #   already set, first removing the final colon that should be
                #   there
                # (This is the old method of setting the RSS; no longer
                #   necessary as of v2.3.602, but retained in case it is useful
                #   in the future)
                container_id = re.sub(r'\:*$', '', stdout_list[1])
                media_data_obj.update_rss_from_id(container_id)

            elif (
                not self.dl_sim_flag \
                and stdout_list[2] == 'Downloading' \
                and stdout_list[3] == 'webpage' \
                and re.search(r'^\[[^\]\:]+\]', stdout_list[0]) \
            ):
                # (The re.search() above excludes [youtube:channel] and
                #   [youtube:playlist], etc)
                self.probable_video_id = re.sub(r'\:*$', '', stdout_list[1])

            elif (
                stdout_list[0] == 'Deleting' \
                and stdout_list[1] == 'original' \
                and stdout_list[2] == 'file' \
                and self.stop_after_merge_flag \
            ):
                # (We were waiting for an FFmpeg to finish, before stopping the
                #   download)
                self.stop_now_flag = True
                self.stop_after_merge_flag = False
                return dl_stat_dict

            elif stdout_list[0][0] == '{':

                # JSON data, the result of a simulated download. Convert to a
                #   python dictionary
                if self.dl_sim_flag:

                    # (Try/except to check for invalid JSON)
                    try:
                        json_dict = json.loads(stdout)

                    except:
                        GObject.timeout_add(
                            0,
                            app_obj.system_error,
                            306,
                            'Invalid JSON data received from server',
                        )

                        return dl_stat_dict

                    if json_dict:

                        # For some Classic Mode custom downloads, Tartube
                        #   performs two consecutive download operations: one
                        #   simulated download to fetch URLs of individual
                        #   videos, and another to download each video
                        #   separately
                        # If we're on the first operation, the dummy
                        #   media.Video object's URL may represent an
                        #   individual video, or a channel or playlist
                        # In both cases, we simply make a list of each video
                        #   detected, along with its metadata, ready for the
                        #   second operation
                        if self.download_item_obj.operation_type \
                        == 'classic_sim':

                            # (If the URL can't be retrieved for any reason,
                            #   then just ignore this batch of JSON)
                            if 'webpage_url' in json_dict:
                                self.download_manager_obj.register_classic_url(
                                    self.download_item_obj.media_data_obj,
                                    json_dict,
                                )

                        # If youtube-dl is about to download a channel or
                        #   playlist into a media.Video object, decide what to
                        #   do to prevent that
                        # The called function returns a True/False value,
                        #   specifically to allow this code block to call
                        #   self.confirm_sim_video when required
                        # v1.3.063 At this point, self.video_num can be 0 for a
                        #   URL that's an individual video, but > 0 for a URL
                        #   that's actually a channel/playlist
                        elif not self.video_num \
                        or self.check_dl_is_correct_type():
                            self.confirm_sim_video(json_dict)

                        self.video_num += 1
                        dl_stat_dict['playlist_index'] = self.video_num
                        self.video_total += 1
                        dl_stat_dict['playlist_size'] = self.video_total

                        dl_stat_dict['status'] = formats.ACTIVE_STAGE_CHECKING

            elif stdout_list[0][0] != '[' or stdout_list[0] == '[debug]':

                # (Just ignore this output)
                return dl_stat_dict

            elif self.video_download_started_flag:

                # The download has already started
                dl_stat_dict['status'] = formats.ACTIVE_STAGE_POST_PROCESS

            else:

                # The download is about to start
                dl_stat_dict['status'] = formats.ACTIVE_STAGE_PRE_PROCESS

        except:

            # !!! DEBUG Git #395
            GObject.timeout_add(
                0,
                app_obj.system_error,
                319,
                'VideoDownloader.extract_stdout_data() index error. This is' \
                + ' an unresolved bug; please show the authors the URL that' \
                + ' caused it, and this text: ' + str(stdout),
                )

        return dl_stat_dict


    def extract_stdout_status(self, dl_stat_dict):

        """Called by self.read_child_process() immediately after a call to
        self.extract_stdout_data().

        Based on YoutubeDLDownloader._extract_info().

        If the job's status is formats.COMPLETED_STAGE_ALREADY or
        formats.ERROR_STAGE_ABORT, translate that into a new value for the
        return code, and then use that value to actually set self.return_code
        (which halts the download).

        Args:

            dl_stat_dict (dict): The Python dictionary returned by the call to
                self.extract_stdout_data(), in the standard form described by
                the comments for that function

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 5714 extract_stdout_status')

        if 'status' in dl_stat_dict:
            if dl_stat_dict['status'] == formats.COMPLETED_STAGE_ALREADY:
                self.set_return_code(self.ALREADY)
                dl_stat_dict['status'] = None

            if dl_stat_dict['status'] == formats.ERROR_STAGE_ABORT:
                self.set_return_code(self.FILESIZE_ABORT)
                dl_stat_dict['status'] = None


    def is_blocked(self, stderr):

        """Called by self.register_error_warning().

        See if a STDERR message indicates a video that is censored, age-
        restricted or otherwise unavailable for download.

        Args:

            stderr (str): A message from the child process STDERR

        Return values:

            True if the video is blocked, False if not

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 5744 is_blocked')

        # N.B. These strings also appear in self.is_ignorable()
        regex_list = [
            'Content Warning',
            'This video may be inappropriate for some users',
            'Sign in to confirm your age',
            'This video contains content from.*copyright grounds',
            'This video requires payment to watch',
            'The uploader has not made this video available',
        ]

        for regex in regex_list:

            if re.search(r'\s*(\S*)\:\s' + regex, stderr):
                return True

        # Not blocked
        return None


    def is_child_process_alive(self):

        """Called by self.do_download() and self.stop().

        Based on YoutubeDLDownloader._proc_is_alive().

        Called continuously during the self.do_download() loop to check whether
        the child process has finished or not.

        Return values:

            True if the child process is alive, otherwise returns False

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 5781 is_child_process_alive')

        if self.child_process is None:
            return False

        return self.child_process.poll() is None


    def is_debug(self, stderr):

        """Called by self.do_download().

        Based on YoutubeDLDownloader._is_warning().

        After the child process has terminated with an error of some kind,
        checks the STERR message to see if it's an error or just a debug
        message (generated then youtube-dl verbose output is turned on).

        Args:

            stderr (str): A message from the child process STDERR

        Return values:

            True if the STDERR message is a youtube-dl debug message, False if
                it's an error

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 5811 is_debug')

        return stderr.split(' ')[0] == '[debug]'


    def is_ignorable(self, stderr):

        """Called by self.register_error_warning().

        Before testing a STDERR message, see if it's one of the frequent
        messages which the user has opted to ignore (if any).

        Args:

            stderr (str): A message from the child process STDERR

        Return values:

            True if the STDERR message is ignorable, False if it should be
                tested further

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 5835 is_ignorable')

        app_obj = self.download_manager_obj.app_obj
        media_data_obj = self.download_item_obj.media_data_obj

        if (
            app_obj.ignore_http_404_error_flag \
            and (
                re.search(
                    r'unable to download video data\: HTTP Error 404',
                    stderr,
                ) or re.search(
                    r'Unable to extract video data',
                    stderr,
                )
            )
        ) or (
            app_obj.ignore_data_block_error_flag \
            and re.search(r'Did not get any data blocks', stderr)
        ) or (
            app_obj.ignore_merge_warning_flag \
            and re.search(
                r'Requested formats are incompatible for merge',
                stderr,
            )
        ) or (
            app_obj.ignore_missing_format_error_flag \
            and re.search(
                r'No video formats found; please report this issue',
                stderr,
            )
        ) or (
            app_obj.ignore_no_annotations_flag \
            and re.search(
                r'There are no annotations to write',
                stderr,
            )
        ) or (
            app_obj.ignore_no_subtitles_flag \
            and re.search(
                r'video doesn\'t have subtitles',
                stderr,
            )
        ) or (
            app_obj.ignore_page_given_flag \
            and re.search(
                r'A channel.user page was given',
                stderr,
            )
        ) or (
            app_obj.ignore_no_descrip_flag \
            and re.search(
                r'There.s no playlist description to write',
                stderr,
            )
        ) or (
            app_obj.ignore_thumb_404_flag \
            and re.search(
                r'Unable to download video thumbnail.*HTTP Error 404',
                stderr,
            )
        ) or (
            app_obj.ignore_twitch_not_live_flag \
            and re.search(
                r'twitch.*The channel is not currently live',
                stderr,
            )
        ) or (
            app_obj.ignore_yt_age_restrict_flag \
            and (
                re.search(
                    r'Content Warning',
                    stderr,
                ) or re.search(
                    r'This video may be inappropriate for some users',
                    stderr,
                ) or re.search(
                    r'Sign in to confirm your age',
                    stderr,
                )
            )
        ) or (
            app_obj.ignore_yt_copyright_flag \
            and (
                re.search(
                    r'This video contains content from.*copyright grounds',
                    stderr,
                ) or re.search(
                    r'Sorry about that\.',
                    stderr,
                )
            )
        ) or (
            app_obj.ignore_yt_payment_flag \
            and re.search(
                r'This video requires payment to watch',
                stderr,
            )

        ) or (
            app_obj.ignore_yt_uploader_deleted_flag \
            and (
                re.search(
                    r'The uploader has not made this video available',
                    stderr,
                )
            )
        ):
            # This message is ignorable
            return True

        # Check the custom list of messages
        for item in app_obj.ignore_custom_msg_list:
            if (
                (not app_obj.ignore_custom_regex_flag) \
                and stderr.find(item) > -1
            ) or (
                app_obj.ignore_custom_regex_flag and re.search(item, stderr)
            ):
                # This message is ignorable
                return True

        # This message is not ignorable
        return False


    def is_network_error(self, stderr):

        """Called by self.read_child_process().

        Try to detect network errors, indicating a stalled download.

        youtube-dl's output is system-dependent, so this function may not
        detect every type of network error.

        Args:

            stderr (str): A message from the child process STDERR

        Return values:

            True if the STDERR message seems to be a network error, False if it
                should be tested further

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 5982 is_network_error')

        if re.search(r'[Uu]nable to download video data', stderr) \
        or re.search(r'[Uu]nable to download webpage', stderr) \
        or re.search(r'[Nn]ame or service not known', stderr) \
        or re.search(r'urlopen error', stderr) \
        or re.search(r'Got server HTTP error', stderr):
            return True
        else:
            return False


    def is_warning(self, stderr):

        """Called by self.do_download().

        Based on YoutubeDLDownloader._is_warning().

        After the child process has terminated with an error of some kind,
        checks the STERR message to see if it's an error or just a warning.

        Args:

            stderr (str): A message from the child process STDERR

        Return values:

            True if the STDERR message is a warning, False if it's an error

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 6014 is_warning')

        return stderr.split(':')[0] == 'WARNING'


    def last_data_callback(self):

        """Called by self.read_child_process().

        Based on YoutubeDLDownloader._last_data_hook().

        After the child process has finished, creates a new Python dictionary
        in the standard form described by self.extract_stdout_data().

        Sets key-value pairs in the dictonary, then passes it to the parent
        downloads.DownloadWorker object, confirming the result of the child
        process.

        The new key-value pairs are used to update the main window.
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 6036 last_data_callback')

        dl_stat_dict = {}

        if self.return_code == self.OK:
            dl_stat_dict['status'] = formats.COMPLETED_STAGE_FINISHED
        elif self.return_code == self.ERROR:
            dl_stat_dict['status'] = formats.MAIN_STAGE_ERROR
            dl_stat_dict['eta'] = ''
            dl_stat_dict['speed'] = ''
        elif self.return_code == self.WARNING:
            dl_stat_dict['status'] = formats.COMPLETED_STAGE_WARNING
            dl_stat_dict['eta'] = ''
            dl_stat_dict['speed'] = ''
        elif self.return_code == self.STOPPED:
            dl_stat_dict['status'] = formats.ERROR_STAGE_STOPPED
            dl_stat_dict['eta'] = ''
            dl_stat_dict['speed'] = ''
        elif self.return_code == self.ALREADY:
            dl_stat_dict['status'] = formats.COMPLETED_STAGE_ALREADY
        elif self.return_code == self.STALLED:
            dl_stat_dict['status'] = formats.MAIN_STAGE_STALLED
        else:
            dl_stat_dict['status'] = formats.ERROR_STAGE_ABORT

        # Use some empty values in dl_stat_dict so that the Progress tab
        #   doesn't show arbitrary data from the last file downloaded
        # Exception: in Classic Mode, don't do that for self.ALREADY, otherwise
        #   the filename will never be visible
        if not self.dl_classic_flag or self.return_code != self.ALREADY:
            dl_stat_dict['filename'] = ''
            dl_stat_dict['extension'] = ''
        dl_stat_dict['percent'] = ''
        dl_stat_dict['eta'] = ''
        dl_stat_dict['speed'] = ''
        dl_stat_dict['filesize'] = ''

        # The True argument shows that this function is the caller
        self.download_worker_obj.data_callback(dl_stat_dict, True)


    def match_vid_or_url(self, media_data_obj, vid, url=None):

        """Called by self.register_error_warning().

        Tests whether a media.Video object has a specified video ID, or a the
        URL expected from that video ID.

        Args:

            media_data_obj (media.Video): The video to test

            vid (str): The video ID

            url (str or None): A URL expected from that video ID, or None if
                we don't know how to convert the video ID into a URL

        Return values:

            True if the video matches the video ID or URL, False otherwise

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 6100 match_vid_or_url')

        if (
            media_data_obj.vid is not None \
            and media_data_obj.vid == vid
        ) or (
            media_data_obj.source is not None \
            and media_data_obj.source == url
        ):
            return True
        else:
            return False


    def process_error_warning(self, vid):

        """Called by downloads.DownloadWorker.run_video_downloader() or by any
        other code.

        When a youtube-dl error/warning message is received with an
        identifiable video ID, the corresponding media.Video object might not
        yet exist.

        The error/warning is stored temporarily in self.video_msg_buffer_dict()
        until it can be passed on to the media.Video. (If the media.Video still
        does not exist, pass it on to the parent channel/playlist instead.)

        Args:

            vid (str): The video ID, a key in self.video_msg_buffer_dict

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 6134 process_error_warning')

        if not vid in self.video_msg_buffer_dict:

            GObject.timeout_add(
                0,
                app_obj.system_error,
                307,
                'Missing VID in video error/warning buffer',
            )

            return

        # Import the main application (for convenience)
        app_obj = self.download_manager_obj.app_obj

        # Search for a matching media.Video
        video_obj = None

        if isinstance(self.download_item_obj.media_data_obj, media.Video):

            # This should not happen, but handle it anyway
            video_obj = self.download_item_obj.media_data_obj

        else:

            for child_obj in self.download_item_obj.media_data_obj.child_list:

                if isinstance(child_obj, media.Video) \
                and child_obj.vid is not None \
                and child_obj.vid == vid:

                    video_obj = child_obj
                    break

        # mini_list is in the form [ msg_type, data ]
        for mini_list in self.video_msg_buffer_dict[vid]:

            if video_obj is None:

                # No matching media.Video found; assign the error/warning to
                #   the parent channel/playlist instead
                if mini_list[0] == 'warning':
                    self.set_return_code(self.WARNING)
                    self.download_item_obj.media_data_obj.set_warning(
                        mini_list[1],
                    )

                else:
                    self.set_return_code(self.ERROR)
                    self.download_item_obj.media_data_obj.set_error(
                        mini_list[1],
                    )

            else:

                if mini_list[0] == 'warning':
                    self.set_warning(video_obj, mini_list[1])
                else:
                    self.set_error(video_obj, mini_list[1])

                # Code in downloads.DownloadWorker.run_video_downloader()
                #   calls mainwin.MainWin.errors_list_add_operation_msg() for
                #   the main downloads.DownloadItem and its errors/warnings;
                #   but for a child video, we have to call it directly
                # The True argument means 'display the last error/warning only'
                #   in case the same video generates several errors
                GObject.timeout_add(
                    0,
                    app_obj.main_win_obj.errors_list_add_operation_msg,
                    video_obj,
                    True,
                )

                GObject.timeout_add(
                    0,
                    app_obj.main_win_obj.video_catalogue_update_video,
                    video_obj,
                )


    def read_child_process(self):

        """Called by self.do_download().

        Reads from the child process STDOUT and STDERR, in the correct order.

        Return values:

            True if either STDOUT or STDERR were read. None if both queues were
                empty, or if STDERR was read and a network error was detected

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 6227 read_child_process')

        # mini_list is in the form [time, pipe_type, data]
        try:
            mini_list = self.queue.get_nowait()

        except:
            # Nothing left to read
            return None

        # Import the main application (for convenience)
        app_obj = self.download_manager_obj.app_obj

        # Failsafe check
        if not mini_list \
        or (mini_list[1] != 'stdout' and mini_list[1] != 'stderr'):

            # Just in case...
            GObject.timeout_add(
                0,
                self.download_manager_obj.app_obj.system_error,
                308,
                'Malformed STDOUT or STDERR data',
            )

        # STDOUT or STDERR has been read
        data = mini_list[2].rstrip()
        # On MS Windows we use cp1252, so that Tartube can communicate with the
        #   Windows console
        data = data.decode(ttutils.get_encoding(), 'replace')

        # youtube-dl livestream downloads are normally handles by
        #   downloads.StreamDownloader, but in certain circumstances this
        #   VideoDownloader might be asked to handle them
        # When youtube-dl is downloading the livestream directly (i.e. without
        #   .m3u), it produces a lot of output in STDERR, most of which can be
        #   ignored, but some of which should be converted to STDOUT
        if mini_list[1] == 'stderr':
            mod_data = ttutils.stream_output_is_ignorable(data)
            if mod_data is None:
                # Ignore whole line
                self.queue.task_done()

                return True
            elif mod_data != data:
                # Ignore the unmatched portion of the line, and convert STDERR
                #   to STDOUT (so self.extract_stdout_data() can process it as
                #   normal)
                data = mod_data
                mini_list[1] = 'stdout'

        # STDOUT
        if mini_list[1] == 'stdout':

            # Look out for network errors that indicate a stalled download
            # (I'm not sure why this message does not appear in STDERR;
            #   self.is_network_error() checks for the same pattern)
            if app_obj.operation_auto_restart_flag \
            and self.network_error_time is None \
            and re.search('Got server HTTP error', data):

                self.network_error_time = time.time()

            else:

                # Convert download statistics into a python dictionary in a
                #   standard format, specified in the comments for
                #   self.extract_stdout_data()
                dl_stat_dict = self.extract_stdout_data(data)
                # If the job's status is formats.COMPLETED_STAGE_ALREADY or
                #   formats.ERROR_STAGE_ABORT, set our self.return_code IV
                self.extract_stdout_status(dl_stat_dict)
                # Pass the dictionary on to self.download_worker_obj so the
                #   main window can be updated
                self.download_worker_obj.data_callback(dl_stat_dict)

            # Show output in the Output tab (if required). For simulated
            #   downloads, a message is displayed by self.confirm_sim_video()
            #   instead
            if app_obj.ytdl_output_stdout_flag \
            and (
                not app_obj.ytdl_output_ignore_progress_flag \
                or not re.search(
                    r'^\[download\]\s+[0-9\.]+\%\sof\s.*\sat\s.*\sETA',
                    data,
                )
            ) and (
                not app_obj.ytdl_output_ignore_json_flag \
                or data[:1] != '{'
            ):
                app_obj.main_win_obj.output_tab_write_stdout(
                    self.download_worker_obj.worker_id,
                    data,
                )

            # Show output in the terminal (if required). For simulated
            #   downloads, a message is displayed by
            #   self.confirm_sim_video() instead
            if app_obj.ytdl_write_stdout_flag \
            and (
                not app_obj.ytdl_write_ignore_progress_flag \
                or not re.search(
                    r'^\[download\]\s+[0-9\.]+\%\sof\s.*\sat\s.*\sETA',
                    data,
                )
            ) and (
                not app_obj.ytdl_write_ignore_json_flag \
                or data[:1] != '{'
            ):
                # Git #175, Japanese text may produce a codec error here,
                #   despite the .decode() call above
                try:
                    print(
                        data.encode(ttutils.get_encoding(), 'replace'),
                    )
                except:
                    print('STDOUT text with unprintable characters')

            # Write output to the download log (if required). For simulated
            #   downloads, a message is displayed by
            #   self.confirm_sim_video() instead
            if app_obj.ytdl_log_stdout_flag \
            and (
                not app_obj.ytdl_log_ignore_progress_flag \
                or not re.search(
                    r'^\[download\]\s+[0-9\.]+\%\sof\s.*\sat\s.*\sETA',
                    data,
                )
            ) and (
                not app_obj.ytdl_log_ignore_json_flag \
                or data[:1] != '{'
            ):
                app_obj.write_downloader_log(data)

        # STDERR (ignoring any empty error messages)
        elif data != '':

            # Look out for network errors that indicate a stalled download
            if app_obj.operation_auto_restart_flag \
            and self.network_error_time is None \
            and self.is_network_error(data):

                self.network_error_time = time.time()

            else:

                # Check for recognised errors/warnings, and update the
                #   appropriate media data object (immediately, if possible, or
                #   later otherwise)
                self.register_error_warning(data)

            # Show output in the Output tab (if required)
            if app_obj.ytdl_output_stderr_flag:
                app_obj.main_win_obj.output_tab_write_stderr(
                    self.download_worker_obj.worker_id,
                    data,
                )

            # Show output in the terminal (if required)
            if app_obj.ytdl_write_stderr_flag:
                # Git #175, Japanese text may produce a codec error here,
                #   despite the .decode() call above
                try:
                    print(data.encode(ttutils.get_encoding(), 'replace'))
                except:
                    print('STDERR text with unprintable characters')

            # Write output to the downloader log (if required)
            if app_obj.ytdl_log_stderr_flag:
                app_obj.write_downloader_log(data)

            # For Tartube's MS Windows portable version, when the whole
            #   installation folder is moved to a new location in the
            #   filesystem, youtube-dl must be uninstalled, then reinstalled
            if re.search('Fatal error in launcher: U', data) \
            and app_obj.ytdl_output_stderr_flag:

                app_obj.main_win_obj.output_tab_write_stderr(
                    self.download_worker_obj.worker_id,
                    self.app_obj.get_downloader() + ': ' \
                    + _('Please reinstall/update your downloader'),
                )

        # Either (or both) of STDOUT and STDERR were non-empty
        self.queue.task_done()
        return True


    def register_error_warning(self, data):

        """Called by self.read_child_process()

        When youtube-dl produces an error or warning (in its STDERR), pass that
        error/warning on to the appropriate media data object: the video
        responsible, if possible, or the parent channel/playlist if not.

        Args:

            data (str): The error/warning message from the child process STDERR

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 6418 register_error_warning')

        # Import the main application (for convenience)
        app_obj = self.download_manager_obj.app_obj

        # Try to identify the video ID that produced the error/warning. As of
        #   v2.3.453, some error/warning messages contain the video ID, others
        #   do not
        msg_type = None
        vid = None
        site_name = None

        if self.is_warning(data):

            self.set_return_code(self.WARNING)
            msg_type = 'warning'

            # e.g. WARNING: [youtube] abcdefgh: here are no annotations
            match = re.search(
                r'^WARNING\:\s*\[([^\]]+)\]\s*(\S+)\s*\:',
                data,
            )

            if match:
                site_name = match.groups()[0]
                vid = match.groups()[1]

        elif not self.is_debug(data):

            self.set_return_code(self.ERROR)
            msg_type = 'error'

            # e.g. ERROR: [youtube] abcdefgh: Sign in to confirm your age
            match = re.search(
                r'^ERROR\:\s*\[([^\]]+)\]\s*(\S+)\s*\:',
                data,
            )

            if match:
                site_name = match.groups()[0]
                vid = match.groups()[1]

        if not msg_type:
            # Not an error/warning
            return

        # If the error/warning marks the video as blocked, we can add it to
        #   the database (to alert the user about its existence)
        new_obj = None
        if app_obj.add_blocked_videos_flag \
        and vid is not None \
        and self.is_blocked(data):

            # Check this video is not already in the parent channel/playlist/
            #   folder
            media_data_obj = self.download_item_obj.media_data_obj
            url = ttutils.convert_enhanced_template_from_json(
                'convert_video_list',
                site_name,
                { 'video_id': vid },
            )

            if isinstance(media_data_obj, media.Video):

                if self.match_vid_or_url(media_data_obj, vid, url):
                    media_data_obj.set_block_flag(True)

            else:

                match_flag = False
                for child_obj in media_data_obj.child_list:

                    if self.match_vid_or_url(child_obj, vid, url):
                        match_flag = True
                        break

                if not match_flag:

                    # Video is not in the database, so add it
                    new_obj = app_obj.add_video(media_data_obj, url)
                    if new_obj:
                        new_obj.set_block_flag(True)
                        new_obj.set_vid(vid)

        # For some reason, YouTube messages giving the (approximate) start time
        #   of a livestream are written to STDERR
        # If the video's ID is recognised, we can update the media.Video
        #   object. However, we won't add a new video to the database;
        #   JSONFetcher can do that
        if new_obj is None \
        and app_obj.enable_livestreams_flag \
        and vid is not None:

            live_data_dict = ttutils.extract_livestream_data(data)
            if live_data_dict:

                # Check this video is not already in the parent channel/
                #   playlist/folder
                media_data_obj = self.download_item_obj.media_data_obj
                url = ttutils.convert_enhanced_template_from_json(
                    'convert_video_list',
                    site_name,
                    { 'video_id': vid },
                )

                if isinstance(media_data_obj, media.Video):

                    if self.match_vid_or_url(media_data_obj, vid, url):
                        GObject.timeout_add(
                            0,
                            app_obj.mark_video_live,
                            media_data_obj,
                            1,
                            live_data_dict,
                        )

                        # (We don't want mainwin.NewbieDialogue to appear in
                        #   this situation)
                        self.download_manager_obj.register_video('other')

                else:

                    for child_obj in media_data_obj.child_list:

                        if self.match_vid_or_url(child_obj, vid, url):
                            GObject.timeout_add(
                                0,
                                app_obj.mark_video_live,
                                child_obj,
                                1,
                                live_data_dict,
                            )

                            self.download_manager_obj.register_video('other')

                            break

                # Not a true error/warning, so don't mark it as one in the code
                #   below
                return

        # Assign the error/warning to a media data object
        if not self.is_ignorable(data):

            # If the error/warning is anonymous (does not contain the video
            #   ID), then we can use the most probable video ID
            if vid is None \
            and app_obj.auto_assign_errors_warnings_flag \
            and self.probable_video_id is not None:
                vid = self.probable_video_id

            # Decide which media data object should have this error/warning
            #   assigned to it
            if self.dl_classic_flag:

                # During Classic Mode downloads, no point trying to assign
                #   errors/warnings to dummy media.Video objects in a channel/
                #   playlist
                if msg_type == 'warning':
                    self.set_warning(
                        self.download_item_obj.media_data_obj,
                        data,
                    )
                else:
                    self.set_error(
                        self.download_item_obj.media_data_obj,
                        data,
                    )

            elif new_obj:

                # We created a new media.Video object just a moment ago, so
                #   assign the error/warning to it directly
                if msg_type == 'warning':
                    self.set_warning(new_obj, data)
                else:
                    self.set_error(new_obj, data)

                # Code in downloads.DownloadWorker.run_video_downloader()
                #   calls mainwin.MainWin.errors_list_add_operation_msg() for
                #   the main downloads.DownloadItem and its errors/warnings;
                #   but for a child video, we have to call it directly
                # The True argument means 'display the last error/warning only'
                #   in case the same video generates several errors
                GObject.timeout_add(
                    0,
                    app_obj.main_win_obj.errors_list_add_operation_msg,
                    new_obj,
                    True,
                )

                GObject.timeout_add(
                    0,
                    app_obj.main_win_obj.video_catalogue_update_video,
                    new_obj,
                )

            elif isinstance(
                self.download_item_obj.media_data_obj,
                media.Video,
            ):
                # We are downloading a single video, so we don't need the video
                #   ID (in which case, the error/warning can be assigned to it
                #   directly)
                if msg_type == 'warning':
                    self.set_warning(
                        self.download_item_obj.media_data_obj,
                        data,
                    )
                else:
                    self.set_error(
                        self.download_item_obj.media_data_obj,
                        data,
                    )

                GObject.timeout_add(
                    0,
                    app_obj.main_win_obj.video_catalogue_update_video,
                    self.download_item_obj.media_data_obj,
                )

            elif vid is None:

                # We are downloading a channel/playlist and the video ID is not
                #   known, so assign the error/warning to the channel/playlist
                if msg_type == 'warning':
                    self.set_warning(
                        self.download_item_obj.media_data_obj,
                        data,
                    )
                else:
                    self.set_error(
                        self.download_item_obj.media_data_obj,
                        data,
                    )

            else:

                # The corresponding media.Video object might not exist yet.
                #   Temporarily store the error/warning in a buffer, so that
                #   the parent downloads.DownloadWorker can retrieve it
                if vid in self.video_msg_buffer_dict:
                    self.video_msg_buffer_dict[vid].append( [msg_type, data] )
                else:
                    self.video_msg_buffer_dict[vid] = [ [msg_type, data] ]


    def set_error(self, media_data_obj, msg):

        """Wrapper for media.Video.set_error().

        Args:

            media_data_obj (media.Video, media.Channel or media.Playlist):
                The media data object to update. Only videos are updated by
                this function

            msg (str): The error message for this video

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 6678 set_error')

        if isinstance(media_data_obj, media.Video):

            if not media_data_obj.dbid in self.video_error_warning_dict:

                # The new error is the first error/warning generated during
                #   this operation; remove any errors/warnings from previous
                #   operations
                media_data_obj.reset_error_warning()
                self.video_error_warning_dict[media_data_obj.dbid] = True

            # Set the new error
            media_data_obj.set_error(msg)


    def set_warning(self, media_data_obj, msg):

        """Wrapper for media.Video.set_warning().

        Args:

            media_data_obj (media.Video, media.Channel or media.Playlist):
                The media data object to update. Only videos are updated by
                this function

            msg (str): The warning message for this video

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 6709 set_warning')

        if isinstance(media_data_obj, media.Video):

            if not media_data_obj.dbid in self.video_error_warning_dict:

                # The new warning is the first error/warning generated during
                #   this operation; remove any errors/warnings from previous
                #   operations
                media_data_obj.reset_error_warning()
                self.video_error_warning_dict[media_data_obj.dbid] = True

            # Set the new warning
            media_data_obj.set_warning(msg)


    def set_return_code(self, code):

        """Called by self.do_download(), .create_child_process(),
        .extract_stdout_status() and .stop().

        Based on YoutubeDLDownloader._set_returncode().

        After the child process has terminated with an error of some kind,
        sets a new value for self.return_code, but only if the new return code
        is higher in the hierarchy of return codes than the current value.

        Args:

            code (int): A return code in the range 0-5

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 6743 set_return_code')

        # (The code -1, STALLED, overrules everything else)
        if code == -1 or code >= self.return_code:
            self.return_code = code


    def set_temp_destination(self, path, filename, extension):

        """Called by self.extract_stdout_data()."""

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 6755 set_temp_destination')

        self.temp_path = path
        self.temp_filename = filename
        self.temp_extension = extension


    def reset_temp_destination(self):

        """Called by self.extract_stdout_data()."""

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 6767 reset_temp_destination')

        self.temp_path = None
        self.temp_filename = None
        self.temp_extension = None


    def stop(self):

        """Called by DownloadWorker.close() and also by
        mainwin.MainWin.on_progress_list_stop_now().

        Terminates the child process and sets this object's return code to
        self.STOPPED.
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 6784 stop')

        if self.is_child_process_alive():

            if os.name == 'nt':
                # os.killpg is not available on MS Windows (see
                #   https://bugs.python.org/issue5115 )
                self.child_process.kill()

                # When we kill the child process on MS Windows the return code
                #   gets set to 1, so we want to reset the return code back to
                #   0
                self.child_process.returncode = 0

            else:
                os.killpg(self.child_process.pid, signal.SIGKILL)

            self.set_return_code(self.STOPPED)


    def stop_soon(self):

        """Can be called by anything. Currently called by
        mainwin.MainWin.on_progress_list_stop_soon().

        Sets the flag that causes this VideoDownloader to stop after the
        current video.
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 6814 stop_soon')

        self.stop_soon_flag = True


class ClipDownloader(object):

    """Called by downloads.DownloadWorker.run_clip_slice_downloader().

    A modified VideoDownloader to download one or more video clips from a
    specified video (rather than downloading the complete video).

    Optionally concatenates the clips back together, which has the effect of
    removing one or more slices from a video.

    Python class to create multiple system child processes, one for each clip.

    Reads from the child process STDOUT and STDERR, having set up a
    downloads.PipeReader object to do so in an asynchronous way.

    Sets self.return_code to a value in the range 0-5, described below. The
    parent downloads.DownloadWorker object checks that return code once this
    object's child process has finished.

    Args:

        download_manager_obj (downloads.DownloadManager): The download manager
            object handling the entire download operation

        download_worker_obj (downloads.DownloadWorker): The parent download
            worker object. The download manager uses multiple workers to
            implement simultaneous downloads. The download manager checks for
            free workers and, when it finds one, assigns it a
            download.DownloadItem object. When the worker is assigned a
            download item, it creates a new instance of this object to
            interface with youtube-dl, and waits for this object to return a
            return code

        download_item_obj (downloads.DownloadItem): The download item object
            describing the URL from which youtube-dl should download clip(s)

    Warnings:

        The calling function is responsible for calling the close() method
        when it's finished with this object, in order for this object to
        properly close down.

    """


    # Attributes (the same set used by VideoDownloader; not all of them are
    #   used by ClipDownloader)


    # Valid values for self.return_code. The larger the number, the higher in
    #   the hierarchy of return codes.
    # Codes lower in the hierarchy (with a smaller number) cannot overwrite
    #   higher in the hierarchy (with a bigger number)
    #
    # 0 - The download operation completed successfully
    OK = 0
    # 1 - A warning occured during the download operation
    WARNING = 1
    # 2 - An error occured during the download operation
    ERROR = 2
    # 3 - The corresponding url video file was larger or smaller from the given
    #   filesize limit
    FILESIZE_ABORT = 3
    # 4 - The video(s) for the specified URL have already been downloaded
    ALREADY = 4
    # 5 - The download operation was stopped by the user
    STOPPED = 5
    # 6 - The download operation has stalled. The parent worker can restart it,
    #   if required
    STALLED = -1


    # Standard class methods


    def __init__(self, download_manager_obj, download_worker_obj, \
    download_item_obj):

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 6898 __init__')

        # IV list - class objects
        # -----------------------
        # The downloads.DownloadManager object handling the entire download
        #   operation
        self.download_manager_obj = download_manager_obj
        # The parent downloads.DownloadWorker object
        self.download_worker_obj = download_worker_obj
        # The downloads.DownloadItem object describing the URL from which
        #   youtube-dl should download video(s)
        self.download_item_obj = download_item_obj

        # The child process created by self.create_child_process()
        self.child_process = None

        # Read from the child process STDOUT (i.e. self.child_process.stdout)
        #   and STDERR (i.e. self.child_process.stderr) in an asynchronous way
        #   by polling this queue.PriorityQueue object
        self.queue = queue.PriorityQueue()
        self.stdout_reader = PipeReader(self.queue, 'stdout')
        self.stderr_reader = PipeReader(self.queue, 'stderr')


        # IV list - other
        # ---------------
        # The current return code, using values in the range 0-5, as described
        #   above
        # The value remains set to self.OK unless we encounter any problems
        # The larger the number, the higher in the hierarchy of return codes.
        #   Codes lower in the hierarchy (with a smaller number) cannot
        #   overwrite higher in the hierarchy (with a bigger number)
        self.return_code = self.OK
        # The time (in seconds) between iterations of the loop in
        #   self.do_download_clips()
        self.sleep_time = 0.1

        # Flag set to True if this download operation was launched from the
        #   Classic Mode tab, False if not (set below)
        self.dl_classic_flag = False
        # Flag set to True if an attempt to copy an original videos' thumbnail
        #   fails (in which case, don't try again)
        self.thumb_copy_fail_flag = False

        # Flag set to True by a call from any function to self.stop_soon()
        # After being set to True, this ClipDownloader should give up after
        #   the next clip has been downloaded
        self.stop_soon_flag = False
        # When self.stop_soon_flag is True, the next call to
        #   self.extract_stdout_data() for a downloaded clip sets this flag to
        #   True, informing self.do_download_clips() that it can stop the child
        #   process
        self.stop_now_flag = False

        # Named for compatibility with VideoDownloader, both IVs are set to the
        #   number of clips that have been downloaded
        self.video_num = 0
        self.video_total = 0

        # The type of download, depending on which function is called:
        #   'chapters':     self.do_download_clips_with_chapters()
        #   'downloader':   self.do_download_clips_with_downloader()
        #   'ffmpeg':       self.do_download_clips_with_ffmpeg()
        #   'slices':       self.do_download_remove_slices()
        self.dl_type = None

        # Used for 'ffmpeg' and 'slices':
        # Output generated by youtube-dl/FFmpeg may vary, depending on the
        #   file format specified. We have to record every file path
        #   we receive; the last path received is the one that remains on the
        #   filesystem (earlier ones are generally deleted).
        # These two variables are reset at the beginning/end of every clip
        # The file path currently being downloaded/processed
        self.dl_path = None
        # Flag set to True when youtube-dl/FFmpeg appears to have finished
        #   downloading/post-processing the clip
        self.dl_confirm_flag = False

        # Used for self.dl_type = 'chapters':
        self.chapter_dest_obj = None
        self.chapter_dest_dir = None
        self.chapter_orig_video_obj = None

        # Used for self.dl_type = 'downloader':
        self.downloader_path_list = []

        # Dictionary of clip titles used during this operation (i.e. when
        #   splitting a video into clips), used to re-name duplicates
        # Not used when removing video slices
        self.clip_title_dict = {}

        # Code
        # ----
        # Initialise IVs
        if self.download_item_obj.operation_classic_flag:
            self.dl_classic_flag = True


    # Public class methods


    def do_download_clips(self):

        """Called by downloads.DownloadWorker.run_clip_slice_downloader().

        Using the URL described by self.download_item_obj (which must
        represent a media.Video object, during a 'custom_real' or
        'classic_custom' download operation), downloads a series of one or more
        clips, using the timestamps specified by the media.Video itself.

        Return values:

            The final return code, a value in the range 0-5 (as described
                above)

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 7016 do_download_clips')

        # Import the main application and video object (for convenience)
        app_obj = self.download_manager_obj.app_obj
        orig_video_obj = self.download_item_obj.media_data_obj

        # Set the default return code. Everything is OK unless we encounter any
        #   problems
        self.return_code = self.OK

        if not self.dl_classic_flag:

            # Reset the errors/warnings stored in the media data object, the
            #   last time it was checked/downloaded
            orig_video_obj.reset_error_warning()

        if orig_video_obj.dbid in app_obj.temp_stamp_buffer_dict:

            # Retrieve the entry from the main application's temporary
            #   timestamp buffer, if it exists
            stamp_list = app_obj.temp_stamp_buffer_dict[orig_video_obj.dbid]
            # (The temporary buffer, once used, must be emptied immediately)
            app_obj.del_temp_stamp_buffer_dict(orig_video_obj.dbid)

            # The first entry in 'stamp_list' is one of the values 'chapters',
            #   'downloader' or 'ffmpeg'; extract it
            dl_mode = stamp_list.pop(0)
            if dl_mode != 'chapters' \
            and dl_mode != 'downloader' \
            and dl_mode != 'ffmpeg':
                app_obj.main_win_obj.output_tab_write_stderr(
                    self.download_worker_obj.worker_id,
                    _('Invalid timestamps in temporary buffer'),
                )

                self.stop()
                return self.ERROR

        else:

            # Otherwise, re-extract timestamps from the video's .info.json or
            #   description file, if allowed
            if app_obj.video_timestamps_re_extract_flag \
            and not orig_video_obj.stamp_list:
                app_obj.update_video_from_json(orig_video_obj, 'chapters')

            if app_obj.video_timestamps_re_extract_flag \
            and not orig_video_obj.stamp_list:
                orig_video_obj.extract_timestamps_from_descrip(app_obj)

            # Check that at least one timestamp now exists
            if not orig_video_obj.stamp_list:
                app_obj.main_win_obj.output_tab_write_stderr(
                    self.download_worker_obj.worker_id,
                    _('No timestamps defined in video\'s timestamp list'),
                )

                self.stop()
                return self.ERROR

            else:
                stamp_list = orig_video_obj.stamp_list.copy()
                dl_mode = 'default'

        # Set the containing folder, creating a media.Folder object and/or a
        #   sub-directory for the video clips, if required
        parent_obj, parent_dir, dest_obj, dest_dir \
        = ttutils.clip_set_destination(app_obj, orig_video_obj)

        if parent_obj is None:

            # Duplicate media.Folder name, this is a fatal error
            app_obj.main_win_obj.output_tab_write_stderr(
                self.download_worker_obj.worker_id,
                _(
                'FAILED: Can\'t create the destination folder either because' \
                + ' a folder with the same name already exists, or because' \
                + ' new folders can\'t be added to the parent folder',
                ),
            )

            self.stop()

            return self.ERROR

        # Download the clips
        if dl_mode == 'chapters':
            return self.do_download_clips_with_chapters(
                orig_video_obj,
                parent_obj,
                parent_dir,
                dest_obj,
                dest_dir,
            )

        elif dl_mode == 'downloader':

            return self.do_download_clips_with_downloader(
                orig_video_obj,
                stamp_list,
                parent_obj,
                parent_dir,
                dest_obj,
                dest_dir,
            )

        else:

            # (dl_mode == 'ffmpeg')
            return self.do_download_clips_with_ffmpeg(
                orig_video_obj,
                stamp_list,
                parent_obj,
                parent_dir,
                dest_obj,
                dest_dir,
            )


    def do_download_clips_with_chapters(self, orig_video_obj, parent_obj,
    parent_dir, dest_obj, dest_dir):

        """Called by self.do_download_clips().

        Downloads video clips using yt-dlp's --split-chapters. A single
        system command is used to download all requested video clips together.

        Args:

            orig_video_obj (media.Video): The video whose clips are being
                downloaded

            parent_obj (media.Folder): orig_video_obj's containing folder

            parent_dir (str): Path to the containing folder's directory in
                Tartube's data folder

            dest_obj (media.Folder): The actual folder to which video clips are
                downloaded, which might be different from 'parent_obj'

            dest_dir (str): Path to the destination folder

        Return values:

            The final return code, a value in the range 0-5 (as described
                above)

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 7166 do_download_clips_with_chapters')

        # Import the main application (for convenience)
        app_obj = self.download_manager_obj.app_obj

        # Set the download type and its associated IVs
        self.dl_type = 'chapters'
        self.chapter_dest_obj = dest_obj
        self.chapter_dest_dir = dest_dir
        self.chapter_orig_video_obj = orig_video_obj

        # Get an output template for these clip(s)
        if self.dl_classic_flag:
            output_template = ttutils.clip_prepare_chapter_output_template(
                app_obj,
                orig_video_obj,
                orig_video_obj.dummy_dir,
            )

        else:
            output_template = ttutils.clip_prepare_chapter_output_template(
                app_obj,
                orig_video_obj,
                dest_dir,
            )

        # Create a temporary directory to which the full video is downloaded
        temp_dir = self.create_temp_dir_for_chapters(orig_video_obj)
        if temp_dir is None:
            self.set_return_code(self.ERROR)
            app_obj.main_win_obj.output_tab_write_stderr(
                self.download_worker_obj.worker_id,
                _('FAILED: Cannot create temporary directory'),
            )

            return

        # Prepare a system command...
        if self.download_manager_obj.custom_dl_obj is not None:
            divert_mode = self.download_manager_obj.custom_dl_obj.divert_mode
        else:
            divert_mode = None

        cmd_list = ttutils.generate_chapters_split_system_cmd(
            app_obj,
            orig_video_obj,
            self.download_worker_obj.options_list.copy(),
            dest_dir,
            temp_dir,
            output_template,
            self.download_manager_obj.custom_dl_obj,
            divert_mode,
            self.dl_classic_flag,
        )

        # ...display it in the Output tab (if required)...
        display_cmd = ttutils.prepare_system_cmd_for_display(cmd_list)
        if app_obj.ytdl_output_system_cmd_flag:
            app_obj.main_win_obj.output_tab_write_system_cmd(
                self.download_worker_obj.worker_id,
                display_cmd,
            )

        # ...and the terminal (if required)
        if app_obj.ytdl_write_system_cmd_flag:
            print(display_cmd)

        # ...and the downloader log (if required)
        if app_obj.ytdl_log_system_cmd_flag:
            app_obj.write_downloader_log(display_cmd)

        # Write an additional message in the Output tab, in the same style
        #   as those produced by youtube-dl/FFmpeg (and therefore not
        #   translated)
        app_obj.main_win_obj.output_tab_write_stdout(
            self.download_worker_obj.worker_id,
            '[' + __main__.__packagename__ + '] Downloading chapters',
        )

        # Create a new child process using that command...
        self.create_child_process(cmd_list)
        # ...and set up the PipeReader objects to read from the child
        #   process STDOUT and STDERR
        if self.child_process is not None:
            self.stdout_reader.attach_fh(self.child_process.stdout)
            self.stderr_reader.attach_fh(self.child_process.stderr)

        # Pass data on to self.download_worker_obj so the main window can be
        #   updated. We don't know for sure how many chapters there will be, so
        #   just use default values
        self.download_worker_obj.data_callback({
            'playlist_index': 1,
            'playlist_size': 1,
            'status': formats.ACTIVE_STAGE_DOWNLOAD,
            'filename': '',
            # This guarantees the the Classic Progress List shows the clip
            #   title, not the original filename
            'clip_flag': True,
        })

        # While downloading the media data object(s), update the callback
        #   function with the status of the current job
        while self.is_child_process_alive():

            # Pause a moment between each iteration of the loop (we don't want
            #   to hog system resources)
            time.sleep(self.sleep_time)

            # Read from the child process STDOUT and STDERR, in the correct
            #   order, until there is nothing left to read
            while self.read_child_process():
                pass

            # Stop this clip downloader, if required to do so
            if self.stop_now_flag:
                self.stop()

        # The child process has finished
        # We also set the return code to self.ERROR if the download didn't
        #   start or if the child process return code is greater than 0
        # Original notes from youtube-dl-gui:
        #   NOTE: In Linux if the called script is just empty Python exits
        #       normally (ret=0), so we can't detect this or similar cases
        #       using the code below
        #   NOTE: In Unix a negative return code (-N) indicates that the child
        #       was terminated by signal N (e.g. -9 = SIGKILL)
        if self.child_process is None:
            self.set_return_code(self.ERROR)
            app_obj.main_win_obj.output_tab_write_stderr(
                self.download_worker_obj.worker_id,
                _('FAILED: Clip download did not start'),
            )

        elif self.child_process.returncode > 0:
            self.set_return_code(self.ERROR)
            app_obj.main_win_obj.output_tab_write_stderr(
                self.download_worker_obj.worker_id,
                    _(
                    'FAILED: Child process exited with non-zero code: {}'
                    ).format(self.child_process.returncode),
            )

        # If at least one clip was extracted...
        if self.video_total:

            # ...then the number of video downloads must be incremented
            self.download_manager_obj.register_video('clip')

            # Delete the original video, if required, and if it's not inside a
            #   channel/playlist
            # (Don't bother trying to delete a 'dummy' media.Video object, for
            #   download operations launched from the Classic Mode tab)
            if app_obj.split_video_auto_delete_flag \
            and not isinstance(orig_video_obj.parent_obj, media.Channel) \
            and not isinstance(orig_video_obj.parent_obj, media.Playlist) \
            and not orig_video_obj.dummy_flag:

                app_obj.delete_video(
                    orig_video_obj,
                    True,           # Delete all files
                    True,           # Don't update Video Index yet
                    True,           # Don't update Video Catalogue yet
                )


            # Open the destination directory, if required to do so
            if dest_dir is not None \
            and app_obj.split_video_auto_open_flag:
                ttutils.open_file(app_obj, dest_dir)

        # Pass a dictionary of values to downloads.DownloadWorker, confirming
        #   the result of the job. The values are passed on to the main
        #   window
        self.last_data_callback()

        # Pass the result back to the parent downloads.DownloadWorker object
        return self.return_code


    def do_download_clips_with_downloader(self, orig_video_obj, stamp_list,
    parent_obj, parent_dir, dest_obj, dest_dir):

        """Called by self.do_download_clips().

        Downloads video clips using yt-dlp's download-sections. A single
        system command is used to download all requested video clips together.

        Args:

            orig_video_obj (media.Video): The video whose clips are being
                downloaded

            stamp_list (list): List in groups of three, in the form
                [start_timestamp, stop_timestamp, clip_title]

            parent_obj (media.Folder): orig_video_obj's containing folder

            parent_dir (str): Path to the containing folder's directory in
                Tartube's data folder

            dest_obj (media.Folder): The actual folder to which video clips are
                downloaded, which might be different from 'parent_obj'

            dest_dir (str): Path to the destination folder

        Return values:

            The final return code, a value in the range 0-5 (as described
                above)

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 7379 do_download_clips_with_downloader')

        # Import the main application (for convenience)
        app_obj = self.download_manager_obj.app_obj

        # Set the download type
        self.dl_type = 'downloader'

        # Create a temporary directory to which the full video is downloaded
        temp_dir = self.create_temp_dir_for_chapters(orig_video_obj)
        if temp_dir is None:
            self.set_return_code(self.ERROR)
            app_obj.main_win_obj.output_tab_write_stderr(
                self.download_worker_obj.worker_id,
                _('FAILED: Cannot create temporary directory'),
            )

            return

        # Prepare a system command...
        if self.download_manager_obj.custom_dl_obj is not None:
            divert_mode = self.download_manager_obj.custom_dl_obj.divert_mode
        else:
            divert_mode = None

        cmd_list = ttutils.generate_downloader_split_system_cmd(
            app_obj,
            orig_video_obj,
            self.download_worker_obj.options_list.copy(),
            dest_dir,
            temp_dir,
            stamp_list,
            self.download_manager_obj.custom_dl_obj,
            divert_mode,
            self.dl_classic_flag,
        )

        # ...display it in the Output tab (if required)...
        display_cmd = ttutils.prepare_system_cmd_for_display(cmd_list)
        if app_obj.ytdl_output_system_cmd_flag:
            app_obj.main_win_obj.output_tab_write_system_cmd(
                self.download_worker_obj.worker_id,
                display_cmd,
            )

        # ...and the terminal (if required)
        if app_obj.ytdl_write_system_cmd_flag:
            print(display_cmd)

        # ...and the downloader log (if required)
        if app_obj.ytdl_log_system_cmd_flag:
            app_obj.write_downloader_log(display_cmd)

        # Write an additional message in the Output tab, in the same style
        #   as those produced by youtube-dl/FFmpeg (and therefore not
        #   translated)
        app_obj.main_win_obj.output_tab_write_stdout(
            self.download_worker_obj.worker_id,
            '[' + __main__.__packagename__ + '] Downloading sections',
        )

        # Create a new child process using that command...
        self.create_child_process(cmd_list)
        # ...and set up the PipeReader objects to read from the child
        #   process STDOUT and STDERR
        if self.child_process is not None:
            self.stdout_reader.attach_fh(self.child_process.stdout)
            self.stderr_reader.attach_fh(self.child_process.stderr)

        # Pass data on to self.download_worker_obj so the main window can be
        #   updated. We don't know for sure how many chapters there will be, so
        #   just use default values
        self.download_worker_obj.data_callback({
            'playlist_index': 1,
            'playlist_size': 1,
            'status': formats.ACTIVE_STAGE_DOWNLOAD,
            'filename': '',
            # This guarantees the the Classic Progress List shows the clip
            #   title, not the original filename
            'clip_flag': True,
        })

        # While downloading the media data object(s), update the callback
        #   function with the status of the current job
        while self.is_child_process_alive():

            # Pause a moment between each iteration of the loop (we don't want
            #   to hog system resources)
            time.sleep(self.sleep_time)

            # Read from the child process STDOUT and STDERR, in the correct
            #   order, until there is nothing left to read
            while self.read_child_process():
                pass

            # Stop this clip downloader, if required to do so
            if self.stop_now_flag:
                self.stop()

        # The child process has finished
        # We also set the return code to self.ERROR if the download didn't
        #   start or if the child process return code is greater than 0
        # Original notes from youtube-dl-gui:
        #   NOTE: In Linux if the called script is just empty Python exits
        #       normally (ret=0), so we can't detect this or similar cases
        #       using the code below
        #   NOTE: In Unix a negative return code (-N) indicates that the child
        #       was terminated by signal N (e.g. -9 = SIGKILL)
        if self.child_process is None:
            self.set_return_code(self.ERROR)
            app_obj.main_win_obj.output_tab_write_stderr(
                self.download_worker_obj.worker_id,
                _('FAILED: Clip download did not start'),
            )

        elif self.child_process.returncode > 0:
            self.set_return_code(self.ERROR)
            app_obj.main_win_obj.output_tab_write_stderr(
                self.download_worker_obj.worker_id,
                    _(
                    'FAILED: Child process exited with non-zero code: {}'
                    ).format(self.child_process.returncode),
            )

        # Set the destination directory, which is different from the current
        #   value, in downloads from the Classic Mode tab
        if self.dl_classic_flag:
            dest_dir = orig_video_obj.dummy_dir

        # self.downloader_path_list contains a list of paths that yt-dlp
        #   attempted to download, hopefully in the same order as 'stamp_list'
        if self.downloader_path_list:

            for i in range(len(self.downloader_path_list)):

                old_path = self.downloader_path_list[i]

                if not os.path.isfile(old_path):
                    continue
                elif i >= len(stamp_list):
                    break

                # List in groups of 3, in the form
                #   [start_stamp, optional_stop_stamp, optional_clip_title]
                mini_list = stamp_list[i]

                # Rename the clip, ready for it to be added to the Tartube
                #   database
                directory, filename, extension \
                = ttutils.extract_path_components(old_path)
                # (This is a scaled-down version of code in
                #   ttutils.clip_prepare_title() )
                orig_name = orig_video_obj.file_name
                if orig_name is None \
                and orig_video_obj.dummy_flag \
                and orig_video_obj.nickname != app_obj.default_video_name:
                    orig_name = orig_video_obj.nickname

                this_title = mini_list[2]
                if this_title is None:
                    this_title = 'Clip'

                if app_obj.split_video_name_mode == 'num':
                    mod_title = str(i + 1)
                elif app_obj.split_video_name_mode == 'clip':
                    mod_title = this_title
                elif app_obj.split_video_name_mode == 'num_clip':
                    mod_title = str(i + 1) + ' ' + this_title
                elif app_obj.split_video_name_mode == 'clip_num':
                    mod_title = this_title + ' ' + str(i + 1)

                elif app_obj.split_video_name_mode == 'orig' \
                or app_obj.split_video_name_mode == 'orig_num':

                    # N.B. We must have a unique clip name, so these two
                    #   settings are combined
                    if orig_name is None:
                        mod_title = str(i + 1)
                    else:
                        mod_title = orig_name + ' ' + str(i + 1)

                elif app_obj.split_video_name_mode == 'orig_clip':

                    if orig_name is None:
                        mod_title = this_title
                    else:
                        mod_title = orig_name + ' ' + this_title

                elif app_obj.split_video_name_mode == 'orig_num_clip':

                    if orig_name is None:
                        mod_title = str(i + 1) + ' ' + this_title
                    else:
                        mod_title = orig_name + ' ' + str(i + 1) + ' ' \
                        + this_title

                elif app_obj.split_video_name_mode == 'orig_clip_num':

                    if orig_name is None:
                        mod_title = this_title + ' ' + str(i + 1)
                    else:
                        mod_title = orig_name + ' ' + this_title + ' ' \
                        + str(i + 1)

                # Failsafe
                if mod_title is None:
                    mod_title = str(i + 1)

                new_path = os.path.abspath(
                    os.path.join(dest_dir, mod_title + extension),
                )

                ttutils.rename_file(app_obj, old_path, new_path)

                if os.path.isfile(new_path):
                    self.confirm_video_clip(
                        dest_obj,
                        dest_dir,
                        orig_video_obj,
                        mod_title,
                        new_path,
                    )

        # If at least one clip was extracted...
        if self.video_total:

            # ...then the number of video downloads must be incremented
            self.download_manager_obj.register_video('clip')

            # Delete the original video, if required, and if it's not inside a
            #   channel/playlist
            # (Don't bother trying to delete a 'dummy' media.Video object, for
            #   download operations launched from the Classic Mode tab)
            if app_obj.split_video_auto_delete_flag \
            and not isinstance(orig_video_obj.parent_obj, media.Channel) \
            and not isinstance(orig_video_obj.parent_obj, media.Playlist) \
            and not orig_video_obj.dummy_flag:

                app_obj.delete_video(
                    orig_video_obj,
                    True,           # Delete all files
                    True,           # Don't update Video Index yet
                    True,           # Don't update Video Catalogue yet
                )

            # Open the destination directory, if required to do so
            if dest_dir is not None \
            and app_obj.split_video_auto_open_flag:
                ttutils.open_file(app_obj, dest_dir)

        # Pass a dictionary of values to downloads.DownloadWorker, confirming
        #   the result of the job. The values are passed on to the main
        #   window
        self.last_data_callback()

        # Pass the result back to the parent downloads.DownloadWorker object
        return self.return_code


    def do_download_clips_with_ffmpeg(self, orig_video_obj, stamp_list,
    parent_obj, parent_dir, dest_obj, dest_dir):

        """Called by self.do_download_clips().

        Downloads video clips using FFmpeg, on clip at a time.

        Args:

            orig_video_obj (media.Video): The video whose clips are being
                downloaded

            stamp_list (list): List in groups of three, in the form
                [start_timestamp, stop_timestamp, clip_title]

            parent_obj (media.Folder): orig_video_obj's containing folder

            parent_dir (str): Path to the containing folder's directory in
                Tartube's data folder

            dest_obj (media.Folder): The actual folder to which video clips are
                downloaded, which might be different from 'parent_obj'

            dest_dir (str): Path to the destination folder

        Return values:

            The final return code, a value in the range 0-5 (as described
                above)

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 7671 do_download_clips_with_ffmpeg')

        # Import the main application (for convenience)
        app_obj = self.download_manager_obj.app_obj

        # Set the download type
        self.dl_type = 'ffmpeg'

        # Download the clips, one at a time
        list_size = len(stamp_list)
        for i in range(list_size):

            # Reset detection variables
            self.dl_path = None
            self.dl_confirm_flag = False

            # List in the form [start_stamp, stop_stamp, clip_title]
            # If 'stop_stamp' is not specified, then 'start_stamp' of the next
            #   clip is used. If there are no more clips, then this clip will
            #   end at the end of the video
            start_stamp, stop_stamp, clip_title \
            = ttutils.clip_extract_data(stamp_list, i)

            # Set a (hopefully unique) clip title
            clip_title = ttutils.clip_prepare_title(
                app_obj,
                orig_video_obj,
                self.clip_title_dict,
                clip_title,
                i + 1,
                list_size,
            )

            self.clip_title_dict[clip_title] = None

            # Prepare a system command...
            if self.download_manager_obj.custom_dl_obj is not None:
                divert_mode \
                = self.download_manager_obj.custom_dl_obj.divert_mode
            else:
                divert_mode = None

            cmd_list = ttutils.generate_ffmpeg_split_system_cmd(
                app_obj,
                orig_video_obj,
                self.download_worker_obj.options_list.copy(),
                dest_dir,
                clip_title,
                start_stamp,
                stop_stamp,
                self.download_manager_obj.custom_dl_obj,
                divert_mode,
                self.dl_classic_flag,
            )

            # ...display it in the Output tab (if required)...
            display_cmd = ttutils.prepare_system_cmd_for_display(cmd_list)
            if app_obj.ytdl_output_system_cmd_flag:
                app_obj.main_win_obj.output_tab_write_system_cmd(
                    self.download_worker_obj.worker_id,
                    display_cmd,
                )

            # ...and the terminal (if required)
            if app_obj.ytdl_write_system_cmd_flag:
                print(display_cmd)

            # ...and the downloader log (if required)
            if app_obj.ytdl_log_system_cmd_flag:
                app_obj.write_downloader_log(display_cmd)

            # Write an additional message in the Output tab, in the same style
            #   as those produced by youtube-dl/FFmpeg (and therefore not
            #   translated)
            app_obj.main_win_obj.output_tab_write_stdout(
                self.download_worker_obj.worker_id,
                '[' + __main__.__packagename__ + '] Downloading clip ' \
                + str(i + 1) + '/' + str(list_size),
            )

            # Create a new child process using that command...
            self.create_child_process(cmd_list)
            # ...and set up the PipeReader objects to read from the child
            #   process STDOUT and STDERR
            if self.child_process is not None:
                self.stdout_reader.attach_fh(self.child_process.stdout)
                self.stderr_reader.attach_fh(self.child_process.stderr)

            # Pass data on to self.download_worker_obj so the main window can
            #   be updated
            self.download_worker_obj.data_callback({
                'playlist_index': i + 1,
                'playlist_size': list_size,
                'status': formats.ACTIVE_STAGE_DOWNLOAD,
                'filename': clip_title,
                # This guarantees the the Classic Progress List shows the clip
                #   title, not the original filename
                'clip_flag': True,
            })

            # While downloading the media data object, update the callback
            #   function with the status of the current job
            while self.is_child_process_alive():

                # Pause a moment between each iteration of the loop (we don't
                #   want to hog system resources)
                time.sleep(self.sleep_time)

                # Read from the child process STDOUT and STDERR, in the correct
                #   order, until there is nothing left to read
                while self.read_child_process():
                    pass

                # Stop this clip downloader, if required to do so, having just
                #   finished downloading a clip
                if self.stop_now_flag:
                    self.stop()

            # The child process has finished
            # We also set the return code to self.ERROR if the download didn't
            #   start or if the child process return code is greater than 0
            # Original notes from youtube-dl-gui:
            #   NOTE: In Linux if the called script is just empty Python exits
            #       normally (ret=0), so we can't detect this or similar cases
            #       using the code below
            #   NOTE: In Unix a negative return code (-N) indicates that the
            #       child was terminated by signal N (e.g. -9 = SIGKILL)
            if self.child_process is None:
                self.set_return_code(self.ERROR)
                app_obj.main_win_obj.output_tab_write_stderr(
                    self.download_worker_obj.worker_id,
                    _('FAILED: Clip download did not start'),
                )

            elif self.child_process.returncode > 0:
                self.set_return_code(self.ERROR)
                app_obj.main_win_obj.output_tab_write_stderr(
                    self.download_worker_obj.worker_id,
                        _(
                        'FAILED: Child process exited with non-zero code: {}'
                        ).format(self.child_process.returncode),
                )

            # General error handling
            if self.return_code != self.OK:
                break

            # Deal with a confirmed download (if any)
            if self.dl_path is not None and self.dl_confirm_flag:

                self.confirm_video_clip(
                    dest_obj,
                    dest_dir,
                    orig_video_obj,
                    clip_title
                )

        # If at least one clip was extracted...
        if self.video_total:

            # ...then the number of video downloads must be incremented
            self.download_manager_obj.register_video('clip')

            # Delete the original video, if required, and if it's not inside a
            #   channel/playlist
            # (Don't bother trying to delete a 'dummy' media.Video object, for
            #   download operations launched from the Classic Mode tab)
            if app_obj.split_video_auto_delete_flag \
            and not isinstance(orig_video_obj.parent_obj, media.Channel) \
            and not isinstance(orig_video_obj.parent_obj, media.Playlist) \
            and not orig_video_obj.dummy_flag:

                app_obj.delete_video(
                    orig_video_obj,
                    True,           # Delete all files
                    True,           # Don't update Video Index yet
                    True,           # Don't update Video Catalogue yet
                )

            # Open the destination directory, if required to do so
            if dest_dir is not None \
            and app_obj.split_video_auto_open_flag:
                ttutils.open_file(app_obj, dest_dir)

        # Pass a dictionary of values to downloads.DownloadWorker, confirming
        #   the result of the job. The values are passed on to the main
        #   window
        self.last_data_callback()

        # Pass the result back to the parent downloads.DownloadWorker object
        return self.return_code


    def do_download_remove_slices(self):

        """Called by downloads.DownloadWorker.run_clip_slice_downloader().

        Modified version of self.do_download_clips().

        The media.Video object specifies one or more video slices that must be
        removed. We start by downloading the video in clips, as before. The
        clips are the portions of the video that we want to keep.

        Then, we concatenate the clips back together, which has the effect of
        'downloading' a video with the specified slices removed.

        Return values:

            The final return code, a value in the range 0-5 (as described
                above)

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 7885 do_download_remove_slices')

        # Import the main application and video object (for convenience)
        app_obj = self.download_manager_obj.app_obj
        orig_video_obj = self.download_item_obj.media_data_obj

        # Set the download type
        self.dl_type = 'slices'

        # Set the default return code. Everything is OK unless we encounter any
        #   problems
        self.return_code = self.OK

        if not self.dl_classic_flag:

            # Reset the errors/warnings stored in the media data object, the
            #   last time it was checked/downloaded
            self.download_item_obj.media_data_obj.reset_error_warning()

        # Contact the SponsorBlock server to update the video's slice data, if
        #   allowed
        # (No point doing it, if the temporary buffer is set)
        if not orig_video_obj.dbid in app_obj.temp_slice_buffer_dict:

            if app_obj.sblock_re_extract_flag \
            and not orig_video_obj.slice_list:
                ttutils.fetch_slice_data(
                    app_obj,
                    orig_video_obj,
                    self.download_worker_obj.worker_id,
                )

            # Check that at least one slice now exists
            if not orig_video_obj.slice_list:

                app_obj.main_win_obj.output_tab_write_stderr(
                    self.download_worker_obj.worker_id,
                    _('No slices defined in video\'s slice list'),
                )

                self.stop()
                return self.ERROR

        # Create a temporary directory for this video so we don't accidentally
        #   overwrite anything
        parent_dir = orig_video_obj.parent_obj.get_actual_dir(app_obj)
        temp_dir = self.create_temp_dir_for_slices(orig_video_obj)
        if temp_dir is None:
            return self.ERROR

        # If the temporary buffer specifies a slice list, use it; otherwise
        #   use the video's actual slice list
        if not orig_video_obj.dbid in app_obj.temp_slice_buffer_dict:
            slice_list = orig_video_obj.slice_list.copy()
            temp_flag = False

        else:
            slice_list = app_obj.temp_slice_buffer_dict[orig_video_obj.dbid]
            # The first entry in 'slice_list' is the value 'default'; remove it
            slice_list.pop(0)

            # (The temporary buffer, once used, must be emptied immediately)
            app_obj.del_temp_slice_buffer_dict(orig_video_obj.dbid)
            temp_flag = True

        # Convert this list from a list of video slices to be removed, to a
        #   list of video clips to be retained
        # The returned list is in groups of two, in the form
        #   [start_time, stop_time]
        # ...where 'start_time' and 'stop_time' are floating-point values in
        #   seconds. 'stop_time' can be None to signify the end of the video,
        #   but 'start_time' is 0 to signify the start of the video
        clip_list = ttutils.convert_slices_to_clips(
            app_obj,
            self.download_manager_obj.custom_dl_obj,
            slice_list,
            temp_flag,
        )

        # Download the clips, one at a time
        confirmed_list = []
        count = 0
        list_size = len(clip_list)
        for mini_list in clip_list:

            count += 1
            start_time = mini_list[0]
            stop_time = mini_list[1]

            # Reset detection variables
            self.dl_path = None
            self.dl_confirm_flag = False

            # Prepare a system command...
            if self.download_manager_obj.custom_dl_obj is not None:
                divert_mode \
                = self.download_manager_obj.custom_dl_obj.divert_mode
            else:
                divert_mode = None

            cmd_list = ttutils.generate_slice_system_cmd(
                app_obj,
                orig_video_obj,
                self.download_worker_obj.options_list.copy(),
                temp_dir,
                count,
                start_time,
                stop_time,
                self.download_manager_obj.custom_dl_obj,
                divert_mode,
                self.dl_classic_flag,
            )

            # ...display it in the Output tab (if required)...
            display_cmd = ttutils.prepare_system_cmd_for_display(cmd_list)
            if app_obj.ytdl_output_system_cmd_flag:
                app_obj.main_win_obj.output_tab_write_system_cmd(
                    self.download_worker_obj.worker_id,
                    display_cmd,
                )

            # ...and the terminal (if required)
            if app_obj.ytdl_write_system_cmd_flag:
                print(display_cmd)

            # ...and the downloader log (if required)
            if app_obj.ytdl_log_system_cmd_flag:
                app_obj.write_downloader_log(display_cmd)

            # Write an additional message in the Output tab, in the same style
            #   as those produced by youtube-dl/FFmpeg (and therefore not
            #   translated)
            app_obj.main_win_obj.output_tab_write_stdout(
                self.download_worker_obj.worker_id,
                '[' + __main__.__packagename__ + '] Downloading clip ' \
                + str(count) + '/' + str(list_size),
            )

            # Create a new child process using that command...
            self.create_child_process(cmd_list)
            # ...and set up the PipeReader objects to read from the child
            #   process STDOUT and STDERR
            if self.child_process is not None:
                self.stdout_reader.attach_fh(self.child_process.stdout)
                self.stderr_reader.attach_fh(self.child_process.stderr)

            # Pass data on to self.download_worker_obj so the main window can
            #   be updated
            if stop_time is not None:
                clip = 'Clip ' + str(start_time) + 's - ' + str(stop_time) \
                + 's'
            else:
                clip = 'Clip ' + str(start_time) + 's - end'

            self.download_worker_obj.data_callback({
                'playlist_index': count,
                'playlist_size': list_size,
                'status': formats.ACTIVE_STAGE_DOWNLOAD,
                'filename': clip,
            })

            # While downloading the media data object, update the callback
            #   function with the status of the current job
            while self.is_child_process_alive():

                # Pause a moment between each iteration of the loop (we don't
                #   want to hog system resources)
                time.sleep(self.sleep_time)

                # Read from the child process STDOUT and STDERR, in the correct
                #   order, until there is nothing left to read
                while self.read_child_process():
                    pass

                # Stop this clip downloader, if required to do so, having just
                #   finished downloading a clip
                if self.stop_now_flag:
                    self.stop()

            # The child process has finished
            # We also set the return code to self.ERROR if the download didn't
            #   start or if the child process return code is greater than 0
            # Original notes from youtube-dl-gui:
            #   NOTE: In Linux if the called script is just empty Python exits
            #       normally (ret=0), so we can't detect this or similar cases
            #       using the code below
            #   NOTE: In Unix a negative return code (-N) indicates that the
            #       child was terminated by signal N (e.g. -9 = SIGKILL)
            if self.child_process is None:
                self.set_return_code(self.ERROR)
                app_obj.main_win_obj.output_tab_write_stderr(
                    self.download_worker_obj.worker_id,
                    _('FAILED: Clip download did not start'),
                )

            elif self.child_process.returncode > 0:
                self.set_return_code(self.ERROR)
                app_obj.main_win_obj.output_tab_write_stderr(
                    self.download_worker_obj.worker_id,
                        _(
                        'FAILED: Child process exited with non-zero code: {}'
                        ).format(self.child_process.returncode),
                )

            # General error handling
            if self.return_code != self.OK:

                break

            # Add a confirmed download to the list
            if self.dl_path is not None and self.dl_confirm_flag:

                confirmed_list.append(self.dl_path)
                self.video_num += 1
                self.video_total += 1

        # If fewer clips than expected were downloaded, then don't use any of
        #   them
        if len(confirmed_list) != len(clip_list):

            self.set_return_code(self.ERROR)

            app_obj.main_win_obj.output_tab_write_stderr(
                self.download_worker_obj.worker_id,
                _('FAILED: One or more clips were not downloaded'),
            )

        else:

            # Otherwise, get the video's (original) file extension from the
            #   first clip
            file_path, file_ext = os.path.splitext(confirmed_list[0])

            # Ordinarily, the user will check a video before custom downloading
            #   it. If not, the media.Video object won't have a .file_name set,
            #   which breaks the code below; in that case, we'll have to
            #   generate a name ourselves
            if orig_video_obj.file_name is None:
                fallback_name = _('Video') + ' ' + str(orig_video_obj.dbid)
                orig_video_obj.set_name(fallback_name)
                orig_video_obj.set_nickname(fallback_name)
                orig_video_obj.set_file(fallback_name, file_ext)

            # If there is more than one clip, they must be concatenated to
            #   produce a single video (like the original video, from which the
            #   video slices have been removed)
            if len(confirmed_list) == 1:
                output_path = confirmed_list[0]

            else:
                # For FFmpeg's benefit, write a text file listing every clip
                line_list = []
                clips_file = os.path.abspath(
                    os.path.join(temp_dir, 'clips.txt'),
                )

                for confirmed_path in confirmed_list:
                    line_list.append('file \'' + confirmed_path + '\'')

                with open(clips_file, 'w') as fh:
                    fh.write('\n'.join(line_list))

                # Prepare the FFmpeg command to concatenate the clips together
                output_path = os.path.abspath(
                    os.path.join(
                        temp_dir,
                        orig_video_obj.file_name + file_ext,
                    ),
                )

                cmd_list = [
                    app_obj.ffmpeg_manager_obj.get_executable(),
                    '-safe',
                    '0',
                    '-f',
                    'concat',
                    '-i',
                    clips_file,
                    '-c',
                    'copy',
                    output_path,
                ]

                # ...display it in the Output tab (if required)...
                if app_obj.ytdl_output_system_cmd_flag:
                    app_obj.main_win_obj.output_tab_write_system_cmd(
                        self.download_worker_obj.worker_id,
                        ' '.join(cmd_list),
                    )

                # ...and the terminal (if required)
                if app_obj.ytdl_write_system_cmd_flag:
                    print(' '.join(cmd_list))

                # ...and the downloader log (if required)
                if app_obj.ytdl_log_system_cmd_flag:
                    app_obj.write_downloader_log(' '.join(cmd_list))

                # Create a new child process using that command...
                self.create_child_process(cmd_list)
                # ...and set up the PipeReader objects to read from the child
                #   process STDOUT and STDERR
                if self.child_process is not None:
                    self.stdout_reader.attach_fh(self.child_process.stdout)
                    self.stderr_reader.attach_fh(self.child_process.stderr)

                # Pass data on to self.download_worker_obj so the main window
                #   can be updated
                self.download_worker_obj.data_callback({
                    'playlist_index': self.video_total,
                    'playlist_size': self.video_total,
                    'status': formats.ACTIVE_STAGE_CONCATENATE,
                    'filename': '',
                })

                # Wait for the concatenation to finish. We are not bothered
                #   about reading the child process STDOUT/STDERR, since we can
                #   just test for the existence of the output file
                while self.is_child_process_alive():
                    time.sleep(self.sleep_time)

                if not os.path.isfile(output_path):

                    app_obj.main_win_obj.output_tab_write_stderr(
                        self.download_worker_obj.worker_id,
                        _('FAILED: Can\'t concatenate clips'),
                    )

                    return self.ERROR

            # Move the single video file back into the parent directory,
            #   replacing any file of the same name that's already there
            moved_path = os.path.abspath(
                os.path.join(
                    parent_dir,
                    orig_video_obj.file_name + file_ext,
                ),
            )

            if os.path.isfile(moved_path):
                app_obj.remove_file(moved_path)

            if not app_obj.move_file_or_directory(output_path, moved_path):
                app_obj.main_win_obj.output_tab_write_stderr(
                    self.download_worker_obj.worker_id,
                    _(
                        'FAILED: Clips were concatenated, but could not move' \
                        + ' the output file out of the temporary directory',
                    ),
                )

                return self.ERROR

            # Also move metadata files, if they don't already exist in the
            #   parent directory (or its /.data and ./thumbs sub-directories)
            self.move_metadata_files(orig_video_obj, temp_dir, parent_dir)

            # Update media.Video IVs (in particular, in some circumstances,
            #   FFmpeg may have switched the file extension to a different one)
            orig_video_obj.set_file(orig_video_obj.file_name, file_ext)

            # downloads.DownloadManager tracks the number of video slices
            #   removed
            for i in range(len(slice_list)):
                self.download_manager_obj.register_slice()

            # Update Tartube's database
            self.confirm_video_remove_slices(orig_video_obj, moved_path)

        # Delete the temporary directory
        app_obj.remove_directory(temp_dir)

        # Pass a dictionary of values to downloads.DownloadWorker, confirming
        #   the result of the job. The values are passed on to the main
        #   window
        self.last_data_callback()

        # Pass the result back to the parent downloads.DownloadWorker object
        return self.return_code


    def close(self):

        """Can be called by anything.

        Destructor function for this object.
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 8274 close')

        # Tell the PipeReader objects to shut down, thus joining their threads
        self.stdout_reader.join()
        self.stderr_reader.join()


    def confirm_video_clip(self, dest_obj, dest_dir, orig_video_obj, \
    clip_title, clip_path=None):

        """Called by self.do_download_clips_with_ffmpeg(),
        self.extract_stdout_data(), etc, when a video clip is confirmed as
        having been downloaded.

        Args:

            dest_obj (media.Folder): The folder object into which the new video
                object is to be created

            dest_dir (str): The path to that folder on the filesystem

            orig_video_obj (media.Video): The original video, from which the
                video clip has been split

            clip_title (str): The clip title for the new video, matching its
                filename

            clip_path (str or None): Full path to the video clip; specified
                only when required

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 8307 confirm_video_clip')

        # Import the main application (for convenience)
        app_obj = self.download_manager_obj.app_obj

        # Download confirmed
        self.video_num += 1
        self.video_total += 1
        self.download_manager_obj.register_clip()

        if dest_obj \
        and app_obj.split_video_add_db_flag \
        and not orig_video_obj.dummy_flag:

            # Add the clip to Tartube's database
            if self.dl_type == 'ffmpeg':

                clip_video_obj = ttutils.clip_add_to_db(
                    app_obj,
                    dest_obj,
                    orig_video_obj,
                    clip_title,
                    self.dl_path,
                )

            elif self.dl_type == 'chapters' or self.dl_type == 'downloader':

                clip_video_obj = ttutils.clip_add_to_db(
                    app_obj,
                    dest_obj,
                    orig_video_obj,
                    clip_title,
                    clip_path,
                )

            if clip_video_obj and not orig_video_obj.dummy_flag:

                # Update the Results List (unless the download operation was
                #   launched from the Classic Mode tab)
                GObject.timeout_add(
                    0,
                    app_obj.main_win_obj.results_list_add_row,
                    self.download_item_obj,
                    clip_video_obj,
                    {},                 # No 'mini_options_dict' to apply
                )

        elif app_obj.split_video_copy_thumb_flag \
        and not self.thumb_copy_fail_flag:

            # The call to ttutils.clip_add_to_db() copies the original
            #   thumbnail, when required
            # Since we're not going to call that, copy the thumbnail here
            thumb_path = ttutils.find_thumbnail(app_obj, orig_video_obj)
            if thumb_path is not None:

                _, thumb_ext = os.path.splitext(thumb_path)
                new_path = os.path.abspath(
                    os.path.join(dest_dir, clip_title + thumb_ext),
                )

                try:

                    shutil.copyfile(thumb_path, new_path)

                except:

                    GObject.timeout_add(
                        0,
                        app_obj.system_error,
                        309,
                        _(
                            'Failed to copy the original video\'s' \
                            + ' thumbnail',
                        ),
                    )

                    # Don't try to copy orig_video_obj's thumbnail again
                    self.thumb_copy_fail_flag = True

        # This ClipDownloader can now stop, if required to do so after a clip
        #   has been downloaded
        if self.stop_soon_flag:
            self.stop_now_flag = True


    def confirm_video_remove_slices(self, orig_video_obj, output_path):

        """Called by self.do_download_remove_slices().

        Once a video has been downloaded as a sequence of clips, then
        concatenated into a single video file (thereby removing one or more
        video slices), make sure the medai.Video object is marked as
        downloaded, and update the main window.

        Args:

            orig_video_obj (media.Video): The video to be downloaded

            output_path (str): Full path to the concatenated video

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 8409 confirm_video_remove_slices')

        # Import the main application (for convenience)
        app_obj = self.download_manager_obj.app_obj

        # Special case: don't add videos to the Tartube database
        if orig_video_obj.parent_obj.dl_no_db_flag:
            # (Do nothing, in this case)
            pass

        # Special case: if the download operation was launched from the
        #   Classic Mode tab, then we only need to update the dummy
        #   media.Video object, and to move/remove description/metadata/
        #   thumbnail files, as appropriate
        elif self.dl_classic_flag:

            orig_video_obj.set_dl_flag(True)
            orig_video_obj.set_dummy_path(output_path)

        elif not orig_video_obj.dl_flag:

            # Mark the video as downloaded
            GObject.timeout_add(
                0,
                app_obj.mark_video_downloaded,
                orig_video_obj,
                True,               # Video is downloaded
            )

            # Do add an entry to the Results List (as well as updating the
            #   Video Catalogue, as normal)
            GObject.timeout_add(
                0,
                app_obj.announce_video_download,
                self.download_item_obj,
                orig_video_obj,
                # No call to ttutils.compile_mini_options_dict(), because this
                #   function deals with download options like
                #   'move_description' by itself
                {},
            )

            # Try to detect the video's new length. The TRUE argument tells
            #   the function to override the existing length, if set
            app_obj.update_video_from_filesystem(
                orig_video_obj,
                output_path,
                True,
            )

        # Register the download with DownloadManager, so that download limits
        #   can be applied, if required
        self.download_manager_obj.register_video('new')

        # Timestamp and slice information is now obsolete for this video, and
        #   can be removed, if required
        if app_obj.slice_video_cleanup_flag:
            orig_video_obj.reset_timestamps()
            orig_video_obj.reset_slices()


    def create_child_process(self, cmd_list):

        """Called by self.do_download_clips() shortly after the call to
        ttutils.generate_ffmpeg_split_system_cmd(), etc.

        Based on YoutubeDLDownloader._create_process().

        Executes the system command, creating a new child process which
        executes youtube-dl.

        Sets self.return_code in the event of an error.

        Args:

            cmd_list (list): Python list that contains the command to execute

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 8489 create_child_process')

        # Strip double quotes from arguments
        # (Since we're sending the system command one argument at a time, we
        #   don't need to retain the double quotes around any single argument
        #   and, in fact, doing so would cause an error)
        cmd_list = ttutils.strip_double_quotes(cmd_list)

        # Create the child process
        info = preexec = None

        if os.name == 'nt':
            # Hide the child process window that MS Windows helpfully creates
            #   for us
            info = subprocess.STARTUPINFO()
            info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        else:
            # Make this child process the process group leader, so that we can
            #   later kill the whole process group with os.killpg
            preexec = os.setsid

        try:
            self.child_process = subprocess.Popen(
                cmd_list,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                preexec_fn=preexec,
                startupinfo=info,
            )

        except (ValueError, OSError) as error:
            # (There is no need to update the media data object's error list,
            #   as the code in self.do_download_clips() will notice the child
            #   process didn't start, and set its own error message)
            self.set_return_code(self.ERROR)


    def create_temp_dir_for_chapters(self, orig_video_obj):

        """Called by self.do_download_clips_with_chapters().

        Create a temporary directory for files used while yt-dlp downloads
        video chapters.

        Args:

            orig_video_obj (media.Video): The video to be downloaded

        Return values:

            The temporary directory created on success, None on failure

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 8544 create_temp_dir_for_chapters')

        # Import the main application (for convenience)
        app_obj = self.download_manager_obj.app_obj

        # Work out where the temporary directory should be...
        temp_dir = os.path.abspath(
            os.path.join(
                app_obj.temp_dir,
                '.clips_' + str(orig_video_obj.dbid)
            ),
        )

        # ...then create it
        try:
            if os.path.isdir(temp_dir):
                app_obj.remove_directory(temp_dir)

            app_obj.make_directory(temp_dir)

            return temp_dir

        except:
            app_obj.main_win_obj.output_tab_write_stderr(
                self.download_worker_obj.worker_id,
                _('FAILED: Can\'t create a temporary folder for video clips'),
            )

            self.stop()

            return None


    def create_temp_dir_for_slices(self, orig_video_obj):

        """Called by self.do_download_remove_slices().

        Before downloading a video in clips, and then concatenating the clips,
        create a temporary directory for the clips so we don't accidentally
        overwrite anything.

        Args:

            orig_video_obj (media.Video): The video to be downloaded

        Return values:

            The temporary directory created on success, None on failure

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 8596 create_temp_dir_for_slices')

        # Import the main application (for convenience)
        app_obj = self.download_manager_obj.app_obj

        # Work out where the temporary directory should be...
        temp_dir = os.path.abspath(
            os.path.join(
                app_obj.temp_dir,
                '.slices_' + str(orig_video_obj.dbid)
            ),
        )

        # ...then create it
        try:
            if os.path.isdir(temp_dir):
                app_obj.remove_directory(temp_dir)

            app_obj.make_directory(temp_dir)

            return temp_dir

        except:
            app_obj.main_win_obj.output_tab_write_stderr(
                self.download_worker_obj.worker_id,
                _('FAILED: Can\'t create a temporary folder for video slices'),
            )

            self.stop()

            return None


    def extract_stdout_data(self, stdout):

        """Called by self.read_child_process().

        Extracts output from the child process.

        Output generated by youtube-dl/FFmpeg may vary, depending on the file
        format specified. We have to record every file path we receive; the
        last path received is the one that remains on the filesystem (earlier
        ones are generally deleted).

        Args:

            stdout (str): String that contains a line from the child process
                STDOUT (i.e. a message from youtube-dl)

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 8648 extract_stdout_data')

        # Import the main application (for convenience)
        app_obj = self.download_manager_obj.app_obj

        # Output received from self.do_download_clips_with_ffmpeg() and
        #   self.do_download_remove_slices()
        if self.dl_type == 'ffmpeg' or self.dl_type == 'slices':

            # Check for a media file being downloaded
            match = re.search(r'^\[download\] Destination\:\s(.*)$', stdout)
            if match:

                self.dl_path = match.group(1)
                return

            match = re.search(r'^\[ffmpeg\] Destination\:\s(.*)$', stdout)
            if match:

                self.dl_path = match.group(1)
                self.dl_confirm_flag = True
                return

            # Check for completion of a media file download
            match = re.search(r'^\[download\] 100% of .* in', stdout)
            if match:

                self.dl_confirm_flag = True
                return

            # Check for confirmation of post-processing
            match = re.search(
                r'^\[ffmpeg\] Merging formats into \"(.*)\"$',
                stdout
            )
            if match:

                self.dl_path = match.group(1)
                self.dl_confirm_flag = True

                return

        elif self.dl_type == 'chapters':

            # !!! DEBUG v2.4.306
            # Would like to extract download progress here, but yt-dlp is
            #   sending all progress updates from 0.1% to 100% in a single line
            #   and not in a consistent way

            # Check for completion of a media file download
            match = re.search(
                r'^\[SplitChapters\] Chapter \d+\; Destination\: (.*)$',
                stdout,
            )
            if match:

                _, name, _ = ttutils.extract_path_components(match.group(1))

                self.confirm_video_clip(
                    self.chapter_dest_obj,
                    self.chapter_dest_dir,
                    self.chapter_orig_video_obj,
                    name,
                    match.group(1),
                )

        elif self.dl_type == 'downloader':

            # Check for the start of a media file download, storing the path
            #   in the list. Hopefully, yt-dlp announces a list of paths that
            #   is in the same order as the sections we specified
            match = re.search(
                r'^\[download\] Destination\: (.*)$',
                stdout,
            )
            if match:
                self.downloader_path_list.append(match.group(1))


    def is_child_process_alive(self):

        """Called by self.do_download_clips(), .do_download_remove_slices and
        .stop().

        Based on YoutubeDLDownloader._proc_is_alive().

        Called continuously during the loop to check whether the child process
        has finished or not.

        Return values:

            True if the child process is alive, otherwise returns False

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 8744 is_child_process_alive')

        if self.child_process is None:
            return False

        return self.child_process.poll() is None


    def is_network_error(self, stderr):

        """Called by self.do_download_clips(); an exact copy of the function in
        VideoDownloader.

        Try to detect network errors, indicating a stalled download.

        youtube-dl's output is system-dependent, so this function may not
        detect every type of network error.

        Args:

            stderr (str): A message from the child process STDERR

        Return values:

            True if the STDERR message seems to be a network error, False if it
                should be tested further

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 8774 is_network_error')

        # v2.3.012, this error is seen on MS Windows:
        #   unable to download video data: <urlopen error [WinError 10060] A
        #   connection attempt failed because the connected party did not
        #   properly respond after a period of time, or established connection
        #   failed because connected host has failed to respond>
        # Don't know yet what the equivalent on other operating systems is, so
        #   we'll detect the first part, which is a string generated by
        #   youtube-dl itself

        if re.search(r'unable to download video data', stderr):
            return True
        else:
            return False


    def last_data_callback(self):

        """Called by self.read_child_process().

        Based on VideoDownloader.last_data_callback().

        After the child process has finished, creates a new Python dictionary
        in the standard form described by self.extract_stdout_data().

        Sets key-value pairs in the dictonary, then passes it to the parent
        downloads.DownloadWorker object, confirming the result of the child
        process.

        The new key-value pairs are used to update the main window.
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 8808 last_data_callback')

        dl_stat_dict = {}

        # (Some of these statuses are not actually used, but the code
        #   references them, in case they are added in future)
        if self.return_code == self.OK:
            dl_stat_dict['status'] = formats.COMPLETED_STAGE_FINISHED
        elif self.return_code == self.ERROR:
            dl_stat_dict['status'] = formats.MAIN_STAGE_ERROR
        elif self.return_code == self.WARNING:
            dl_stat_dict['status'] = formats.COMPLETED_STAGE_WARNING
        elif self.return_code == self.STOPPED:
            dl_stat_dict['status'] = formats.ERROR_STAGE_STOPPED
        elif self.return_code == self.ALREADY:
            dl_stat_dict['status'] = formats.COMPLETED_STAGE_ALREADY
        elif self.return_code == self.STALLED:
            dl_stat_dict['status'] = formats.MAIN_STAGE_STALLED
        else:
            dl_stat_dict['status'] = formats.ERROR_STAGE_ABORT

        # In the Classic Progress List, the 'Incoming File' column showed
        #   clipped names. Replace that with the full video name
        dl_stat_dict['filename'] = self.download_item_obj.media_data_obj.name
        dl_stat_dict['clip_flag'] = True

        # The True argument shows that this function is the caller
        self.download_worker_obj.data_callback(dl_stat_dict, True)


    def move_metadata_files(self, orig_video_obj, temp_dir, parent_dir):

        """Called by self.do_download_remove_slices().

        After moving the (concatenated) video file from its temporary directory
        into the parent container's directory, do the same to the metadata
        files.

        Depending on settings in the options.OptionsManager, they may be
        moved into a sub-directory of the parent cotainer's directory instead.

        Args:

            orig_video_obj (media.Video): The video that was downloaded as a
                sequence of clips

            temp_dir (str): Full path to the temporary directory into which the
                video and its metadata files was downloaded

            parent_dir (str): Full path to the parent container's directory

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 8862 move_metadata_files')

        # Import the main application (for convenience)
        app_obj = self.download_manager_obj.app_obj

        # Handle the description file
        options_obj = self.download_worker_obj.options_manager_obj
        if options_obj.options_dict['keep_description']:

            descrip_path = os.path.abspath(
                os.path.join(temp_dir, 'clip_1.description'),
            )

            if os.path.isfile(descrip_path):

                moved_path = os.path.abspath(
                    os.path.join(
                        parent_dir,
                        orig_video_obj.file_name + '.description',
                    ),
                )

                if options_obj.options_dict['move_description']:
                    final_path = os.path.abspath(
                        os.path.join(
                            parent_dir,
                            '.data',
                            orig_video_obj.file_name + '.description',
                        ),
                    )
                else:
                    final_path = moved_path

                if not os.path.isfile(moved_path) \
                and not os.path.isfile(final_path):
                    app_obj.move_file_or_directory(descrip_path, moved_path)

                    # Further move the file into its sub-directory, if
                    #   required, first creating that sub-directory if it
                    #   doesn't exist
                    if options_obj.options_dict['move_description']:
                        ttutils.move_metadata_to_subdir(
                            app_obj,
                            orig_video_obj,
                            '.description',
                        )

        # Handle the .info.json file
        if options_obj.options_dict['keep_info']:

            json_path = os.path.abspath(
                os.path.join(temp_dir, 'clip_1.info.json'),
            )

            if os.path.isfile(json_path):

                moved_path = os.path.abspath(
                    os.path.join(
                        parent_dir,
                        orig_video_obj.file_name + '.info.json',
                    ),
                )

                if options_obj.options_dict['move_info']:
                    final_path = os.path.abspath(
                        os.path.join(
                            parent_dir,
                            '.data',
                            orig_video_obj.file_name + '.info.json',
                        ),
                    )
                else:
                    final_path = moved_path

                if not os.path.isfile(moved_path) \
                and not os.path.isfile(final_path):
                    app_obj.move_file_or_directory(json_path, moved_path)

                    if options_obj.options_dict['move_info']:
                        ttutils.move_metadata_to_subdir(
                            app_obj,
                            orig_video_obj,
                            '.info.json',
                        )

        # v2.1.101 - Annotations were removed by YouTube in 2019, so this
        #   feature is not available, and will not be available until the
        #   authors have some annotations to test
#       if options_obj.options_dict['keep_annotations']:
#
#           xml_path = os.path.abspath(
#               os.path.join(temp_dir, 'clip_1.annotations.xml'),
#           )
#
#           if os.path.isfile(xml_path):
#
#               moved_path = os.path.abspath(
#                   os.path.join(
#                       parent_dir,
#                       orig_video_obj.file_name + '.annotations.xml',
#                   ),
#               )
#
#               if options_obj.options_dict['move_annotations']:
#                   final_path = os.path.abspath(
#                       os.path.join(
#                           parent_dir,
#                           '.data',
#                           orig_video_obj.file_name + '.annotations.xml',
#                       ),
#                   )
#               else:
#                   final_path = moved_path
#
#               if not os.path.isfile(moved_path) \
#               and not os.path.isfile(final_path):
#                   app_obj.move_file_or_directory(xml_path, moved_path)
#
#                   if options_obj.options_dict['move_annotations']:
#                       ttutils.move_metadata_to_subdir(
#                           app_obj,
#                           orig_video_obj,
#                           '.annotations.xml',
#                       )

        # Handle the thumbnail
        if options_obj.options_dict['keep_thumbnail']:

            thumb_path = ttutils.find_thumbnail_from_filename(
                app_obj,
                temp_dir,
                'clip_1',
            )

            if thumb_path is not None and os.path.isfile(thumb_path):

                name, ext = os.path.splitext(thumb_path)

                moved_path = os.path.abspath(
                    os.path.join(
                        parent_dir,
                        orig_video_obj.file_name + ext,
                    ),
                )

                if not os.path.isfile(moved_path):
                    app_obj.move_file_or_directory(thumb_path, moved_path)

                    # Convert .webp thumbnails to .jpg, if required
                    convert_path \
                    = ttutils.find_thumbnail_webp_intact_or_broken(
                        app_obj,
                        orig_video_obj,
                    )
                    if convert_path is not None \
                    and not app_obj.ffmpeg_fail_flag \
                    and app_obj.ffmpeg_convert_webp_flag \
                    and not app_obj.ffmpeg_manager_obj.convert_webp(
                        convert_path,
                    ):
                        app_obj.set_ffmpeg_fail_flag(True)
                        GObject.timeout_add(
                            0,
                            app_obj.system_error,
                            310,
                            app_obj.ffmpeg_fail_msg,
                        )

                    # Move to the sub-directory, if required
                    if options_obj.options_dict['move_thumbnail']:
                        ttutils.move_thumbnail_to_subdir(
                            app_obj,
                            orig_video_obj,
                        )


    def read_child_process(self):

        """Called by self.do_download_clips() and
        self.do_download_remove_slices().

        Reads from the child process STDOUT and STDERR, in the correct order.

        Return values:

            True if either STDOUT or STDERR were read, None if both queues were
                empty

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 9052 read_child_process')

        # mini_list is in the form [time, pipe_type, data]
        try:
            mini_list = self.queue.get_nowait()

        except:
            # Nothing left to read
            return None

        # Import the main application (for convenience)
        app_obj = self.download_manager_obj.app_obj

        # Failsafe check
        if not mini_list \
        or (mini_list[1] != 'stdout' and mini_list[1] != 'stderr'):

            # Just in case...
            GObject.timeout_add(
                0,
                self.download_manager_obj.app_obj.system_error,
                311,
                'Malformed STDOUT or STDERR data',
            )

        # STDOUT or STDERR has been read
        data = mini_list[2].rstrip()
        # On MS Windows we use cp1252, so that Tartube can communicate with the
        #   Windows console
        data = data.decode(ttutils.get_encoding(), 'replace')

        # STDOUT
        if mini_list[1] == 'stdout':

            # Remove weird carriage returns that insert empty lines into the
            #   Output tab
            data = re.sub(r'[\r]+', '', data)

            # Extract output from STDOUT
            self.extract_stdout_data(data)

            # Show output in the Output tab (if required)
            if app_obj.ytdl_output_stdout_flag:

                app_obj.main_win_obj.output_tab_write_stdout(
                    self.download_worker_obj.worker_id,
                    data,
                )

            # Show output in the terminal (if required)
            if app_obj.ytdl_write_stdout_flag:

                # Git #175, Japanese text may produce a codec error
                #   here, despite the .decode() call above
                try:
                    print(
                        data.encode(
                            ttutils.get_encoding(),
                            'replace',
                        ),
                    )
                except:
                    print(
                        'STDOUT text with unprintable characters'
                    )

            # Write output in the downloader log (if required)
            if app_obj.ytdl_output_stdout_flag:
                app_obj.write_downloader_log(data)

        # STDERR (ignoring any empty error messages)
        elif data != '':

            # v2.3.168 I'm not sure that any detectable errors are actually
            #   produced, but nevertheless this section can handle any such
            #   errors

            # After a network error, stop trying to download clips
            if self.is_network_error(data):

                self.stop()
                self.last_data_callback()
                self.set_return_code(self.STALLED)

                self.queue.task_done()
                return None

            # Show output in the Output tab (if required)
            if app_obj.ytdl_output_stderr_flag:
                app_obj.main_win_obj.output_tab_write_stderr(
                    self.download_worker_obj.worker_id,
                    data,
                )

            # Show output in the terminal (if required)
            if app_obj.ytdl_write_stderr_flag:
                # Git #175, Japanese text may produce a codec error here,
                #   despite the .decode() call above
                try:
                    print(data.encode(ttutils.get_encoding(), 'replace'))
                except:
                    print('STDERR text with unprintable characters')

            # Write output to the downloader log (if required)
            if app_obj.ytdl_log_stderr_flag:
                app_obj.write_downloader_log(data)

        # Either (or both) of STDOUT and STDERR were non-empty
        self.queue.task_done()
        return True


    def set_return_code(self, code):

        """Called by self.do_download_clips(), .do_download_remove_slices(),
        .create_child_process() and .stop().

        Based on YoutubeDLDownloader._set_returncode().

        After the child process has terminated with an error of some kind,
        sets a new value for self.return_code, but only if the new return code
        is higher in the hierarchy of return codes than the current value.

        Args:

            code (int): A return code in the range 0-5

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 9182 set_return_code')

        if code >= self.return_code:
            self.return_code = code


    def stop(self):

        """Called by DownloadWorker.close() and also by
        mainwin.MainWin.on_progress_list_stop_now().

        Terminates the child process and sets this object's return code to
        self.STOPPED.
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 9198 stop')

        if self.is_child_process_alive():

            if os.name == 'nt':
                # os.killpg is not available on MS Windows (see
                #   https://bugs.python.org/issue5115 )
                self.child_process.kill()

                # When we kill the child process on MS Windows the return code
                #   gets set to 1, so we want to reset the return code back to
                #   0
                self.child_process.returncode = 0

            else:
                os.killpg(self.child_process.pid, signal.SIGKILL)

            self.set_return_code(self.STOPPED)


    def stop_soon(self):

        """Can be called by anything. Currently called by
        mainwin.MainWin.on_progress_list_stop_soon().

        Sets the flag that causes this ClipDownloader to stop after the
        current video.
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 9228 stop_soon')

        self.stop_soon_flag = True


class StreamDownloader(object):

    """Called by downloads.DownloadWorker.run_stream_downloader().

    Python class to create a system child process. Uses the child process to
    download a currently broadcasting livestream, using the URL described by a
    downloads.DownloadItem object.

    Reads from the child process STDOUT and STDERR, having set up a
    downloads.PipeReader object to do so in an asynchronous way.

    Sets self.return_code to a value in the range 0-5, described below. The
    parent downloads.DownloadWorker object checks that return code once this
    object's child process has finished.

    Args:

        download_manager_obj (downloads.DownloadManager): The download manager
            object handling the entire download operation

        download_worker_obj (downloads.DownloadWorker): The parent download
            worker object. The download manager uses multiple workers to
            implement simultaneous downloads. The download manager checks for
            free workers and, when it finds one, assigns it a
            download.DownloadItem object. When the worker is assigned a
            download item, it creates a new instance of this object to
            interface with youtube-dl, and waits for this object to return a
            return code

        download_item_obj (downloads.DownloadItem): The download item object
            describing the URL with which the livestream must be downloaded

    Warnings:

        The calling function is responsible for calling the close() method
        when it's finished with this object, in order for this object to
        properly close down.

    """

    # Attributes


    # Valid vlues for self.return_code, following the model established by
    #   downloads.VideoDownloader (but with a smaller set of values)
    # 0 - The download operation completed successfully
    OK = 0
    # 2 - An error occured during the download operation
    ERROR = 2
    # 5 - The download operation was stopped by the user
    STOPPED = 5


    # Standard class methods


    def __init__(self, download_manager_obj, download_worker_obj, \
    download_item_obj):

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 9293 __init__')

        # IV list - class objects
        # -----------------------
        # The downloads.DownloadManager object handling the entire download
        #   operation
        self.download_manager_obj = download_manager_obj
        # The parent downloads.DownloadWorker object
        self.download_worker_obj = download_worker_obj
        # The downloads.DownloadItem object describing the URL of the
        #   broadcasting livestream
        self.download_item_obj = download_item_obj

        # The child process created by self.create_child_process()
        self.child_process = None

        # Read from the child process STDOUT (i.e. self.child_process.stdout)
        #   and STDERR (i.e. self.child_process.stderr) in an asynchronous way
        #   by polling this queue.PriorityQueue object
        self.queue = queue.PriorityQueue()
        self.stdout_reader = PipeReader(self.queue, 'stdout')
        self.stderr_reader = PipeReader(self.queue, 'stderr')


        # IV list - other
        # ---------------
        # The current return code, using values in the range 0-5, as described
        #   above
        # The value remains set to self.OK unless we encounter any problems
        # The larger the number, the higher in the hierarchy of return codes.
        #   Codes lower in the hierarchy (with a smaller number) cannot
        #   overwrite higher in the hierarchy (with a bigger number)
        self.return_code = self.OK
        # The time (in seconds) between iterations of the loop in
        #   self.do_download_basic()
        self.sleep_time = 0.5
        # The time (in seconds) between iterations of the loop in
        #   self.do_download_m3u() and .do_download_streamlink()
        self.longer_sleep_time = 0.25
        # Flag set to True after the first error message processed
        self.first_error_flag = False

        # Shortcut to the livestream download mode: 'default', 'default_mu3' or
        #   'streamlink'
        self.dl_mode = self.download_manager_obj.app_obj.livestream_dl_mode

        # Flag set to True when we're expecting the .m3u manifest in STDOUT,
        #   set back to False when it is received
        self.m3u_waiting_flag = False
        # The text of the .m3u manifest, when received. Stored here so that
        #   self.do_download_m3u() can retrieve it
        self.m3u_manifest = None

        # The actual (video) output path, set when intercepted (and used to
        #   update the Progress List)
        # (YouTube and other sites add a date/time to the video title, which
        #   chnages every minutes; so the output path may not be the one we
        #   were expecting)
        self.actual_output_path = None
        # ...and its components (for quick lookup)
        self.actual_output_dir = None
        self.actual_output_filename = None
        self.actual_output_ext = None
        # The expected output path. In some modes, it is passed directly to the
        #   downloader
        self.expect_output_path = self.choose_path()

        # Flag set to True for downloads in 'streamlink' mode, when the
        #   download started message is detected. The actual output path is on
        #   the next line of STDOU; when this flag is True, that output path
        #   can be intercepted
        self.streamlink_start_flag = False

        # Number of segments downloaded so far
        self.segment_count = 0
        # The time at which we should stop waiting for the next segment
        #   (matches time.time())
        self.check_time = 0
        # Size of the output file, and the time (matches time.time()) at which
        #   this value was set
        # (These IVs are only use by 'default_m3u' and 'streamlink' modes
        self.output_size = 0
        self.output_size_time = 0


    # Public class methods


    def do_download(self):

        """Called by downloads.DownloadWorker.run_stream_downloader().

        Downloads a broadcasting livestream using the URL described by
        self.download_item_obj.

        Return values:

            The final return code, a value in the range 0-5 (as described
                above)

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 9396 do_download')

        # Import the main application (for convenience)
        app_obj = self.download_manager_obj.app_obj
        video_obj = self.download_item_obj.media_data_obj

        # Set the default return code. Everything is OK unless we encounter any
        #   problems
        self.set_return_code(self.OK)

        if not self.download_item_obj.operation_classic_flag:

            # Reset the errors/warnings stored in the media data object, the
            #   last time it was checked/downloaded
            video_obj.reset_error_warning()
            video_obj.set_block_flag(False)

        # If the file already exists (indicating an incomplete livestream
        #   download), we can replace it before re-starting the download, if
        #   required
        if app_obj.livestream_replace_flag \
        and video_obj.file_name is not None:

            if os.path.isfile(self.expect_output_path):
                app_obj.remove_file(self.expect_output_path)

            part_path = self.expect_output_path + '.part'
            if os.path.isfile(part_path):
                app_obj.remove_file(part_path)

        # There are currently three download methods, specified by self.dl_mode
        msg = _('Tartube is starting the livestream download')
        if self.dl_mode == 'default':

            self.show_msg(msg + ' (' + app_obj.get_downloader() + ')...')
            self.do_download_basic()

        elif self.dl_mode == 'default_m3u':

            self.show_msg(
                msg + ' (' + app_obj.get_downloader() + '/FFmpeg/.m3u)...',
            )
            self.do_download_m3u()

        elif self.dl_mode == 'streamlink':

            self.show_msg(msg + ' (streamlink)...')
            self.do_download_streamlink()

        else:

            GObject.timeout_add(
                0,
                app_obj.system_error,
                312,
                _('Invalid livestream download mode'),
            )

            self.set_return_code(self.ERROR)

        # If the file described by the output path actually exists, we can mark
        #   the video as downloaded
        if self.return_code == self.ERROR \
        or self.actual_output_path is None \
        or (
            not os.path.isfile(self.actual_output_path) \
            and not os.path.isfile(self.actual_output_path + '.part')
        ):
            # Video is not marked as downloaded
            self.show_error('Livestream download failed')
            self.set_error(video_obj, 'Livestream download failed')

        else:

            # Because of YouTube's delightful habit of appending the date/time
            #   to a livestream video's title, the media.Video's .file_name
            #   may be different to the name of the file actually downloaded
            # Rectify the situation by renaming the video and/or the .part file
            if not os.path.isfile(self.expect_output_path) \
            and os.path.isfile(self.actual_output_path):

                app_obj.move_file_or_directory(
                    self.actual_output_path,
                    self.expect_output_path,
                )

            if not os.path.isfile(self.expect_output_path + '.part') \
            and os.path.isfile(self.actual_output_path + '.part'):

                app_obj.move_file_or_directory(
                    self.actual_output_path + '.part',
                    self.expect_output_path + '.part',
                )

            # If we have a .part file instead of a video file, we can
            #   optionally salvage the download by converting it (e.g.
            #   convert output.mp4.part to output.mp4, and hope it works)
            if not os.path.isfile(self.expect_output_path) \
            and os.path.isfile(self.expect_output_path + '.part'):

                if app_obj.livestream_stop_is_final_flag:

                    self.show_msg(
                        _(
                            'Incomplete livestream download detected;' \
                            + ' removing the .part component from the' \
                            + ' output file',
                        ),
                    )

                    app_obj.move_file_or_directory(
                        part_path,
                        self.expect_output_path,
                    )

                elif not self.download_item_obj.operation_classic_flag:

                    self.show_msg(
                        _(
                            'Incomplete livestream download detected;' \
                            + ' to complete the download, right-click the' \
                            + ' video and select \'Finalise livestream\'',
                        ),
                    )

            # Update IVs and the main window
            if self.return_code == self.STOPPED \
            and not app_obj.livestream_stop_is_final_flag:

                # Video is not marked as downloaded
                self.show_msg('Livestream download stopped')

            else:

                # Video is marked as downloaded
                if self.return_code == self.STOPPED:
                    self.show_msg('Livestream download stopped')
                else:
                    self.show_msg('Livestream download complete')

                if not self.download_item_obj.operation_classic_flag:

                    # Download from the Videos tab
                    GObject.timeout_add(
                        0,
                        app_obj.mark_video_downloaded,
                        video_obj,
                        True,               # Video is downloaded
                    )
                    GObject.timeout_add(
                        0,
                        app_obj.mark_video_live,
                        video_obj,
                        0,                  # Not live
                    )

                else:

                    # Download from the Classic Mode tab
                    video_obj.set_dl_flag(True)
                    if os.path.isfile(self.expect_output_path):
                        video_obj.set_dummy_path(
                            self.expect_output_path,
                        )
                    else:
                        video_obj.set_dummy_path(
                            self.expect_output_path + '.part',
                        )

                # Update the main window
                GObject.timeout_add(
                    0,
                    app_obj.announce_video_download,
                    self.download_item_obj,
                    video_obj,
                    ttutils.compile_mini_options_dict(
                        self.download_worker_obj.options_manager_obj,
                    ),
                )

                # Register the download with DownloadManager, so that download
                #   limits can be applied, if required
                # (Use 'new' rather than 'old', even though the media.Video
                #   object already exists; the download operation's
                #   confirmation window will be less confusing that way)
                self.download_manager_obj.register_video('new')

        # Pass a dictionary of values to downloads.DownloadWorker, confirming
        #   the result of the job. The values are passed on to the main window
        self.last_data_callback()

        # Pass the result back to the parent downloads.DownloadWorker object
        return self.return_code


    def do_download_basic(self):

        """Called by self.do_download() when self.dl_mode is set to 'default'.

        Downloads a broadcasting livestream using youtube-dl alone.

        This function is based on VideoDownload.do_download() (but simplified,
        because self.download_item_obj.media_data_obj is always a media.Video).
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 9602 do_download_basic')

        # Import the main application (for convenience)
        app_obj = self.download_manager_obj.app_obj

        # Prepare a system command
        options_obj = self.download_worker_obj.options_manager_obj
        if options_obj.options_dict['direct_cmd_flag']:

            cmd_list = ttutils.generate_direct_system_cmd(
                app_obj,
                self.download_item_obj.media_data_obj,
                options_obj,
            )

        else:

            cmd_list = ttutils.generate_ytdl_system_cmd(
                app_obj,
                self.download_item_obj.media_data_obj,
                self.download_worker_obj.options_list,
            )

        # Display the (modified) command in the Output tab and/or terminal (if
        #   required)...
        if app_obj.ytdl_output_system_cmd_flag:
            self.show_cmd(ttutils.prepare_system_cmd_for_display(cmd_list))

        # Create a new child process using that command...
        self.create_child_process(cmd_list)
        # ...and set up the PipeReader objects to read from the child process
        #   STDOUT and STDERR
        if self.child_process is not None:
            self.stdout_reader.attach_fh(self.child_process.stdout)
            self.stderr_reader.attach_fh(self.child_process.stderr)

        # While downloading the media data object, update the callback function
        #   with the status of the current job
        while self.is_child_process_alive():

            # Pause a moment between each iteration of the loop (we don't want
            #   to hog system resources)
            time.sleep(self.sleep_time)

            # Read from the child process STDOUT and STDERR, in the correct
            #   order, until there is nothing left to read
            while self.read_child_process():
                pass

            # Perform a timeout, if necessary
            if self.check_time > 0 and self.check_time < time.time():

                # Halt the child process
                self.stop()
                self.show_msg('Download timed out')
                return

        # The child process has finished
        # We also set the return code to self.ERROR if the download didn't
        #   start or if the child process return code is greater than 0
        # Original notes from youtube-dl-gui:
        #   NOTE: In Linux if the called script is just empty Python exits
        #       normally (ret=0), so we can't detect this or similar cases
        #       using the code below
        #   NOTE: In Unix a negative return code (-N) indicates that the child
        #       was terminated by signal N (e.g. -9 = SIGKILL)
        internal_msg = None
        if self.child_process is None:
            self.set_return_code(self.ERROR)
            internal_msg = _('Download did not start')

        elif self.child_process.returncode > 0:
            self.set_return_code(self.ERROR)
            if not app_obj.ignore_child_process_exit_flag:
                internal_msg = _(
                    'Child process exited with non-zero code: {}',
                ).format(self.child_process.returncode)

        if internal_msg:

            # (The message must be visible in the Errors/Warnings tab, the
            #   Output tab and/or the terminal)
            self.set_error(
                self.download_item_obj.media_data_obj,
                internal_msg,
            )

            self.show_error(internal_msg)

        return


    def do_download_m3u(self):

        """Called by self.do_download() when self.dl_mode is set to
        'default_m3u'.

        Downloads a broadcasting livestream, instructing youtube-dl to fetch
        the .m3u manifest first.
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 9704 do_download_m3u')

        # Import the main application (for convenience)
        app_obj = self.download_manager_obj.app_obj

        # Prepare a system command to fetch the .m3u manifest...
        cmd_list = ttutils.generate_m3u_system_cmd(
            app_obj,
            self.download_item_obj.media_data_obj,
        )

        # ...and display it in the Output tab and/or terminal, if required
        self.show_cmd(ttutils.prepare_system_cmd_for_display(cmd_list))

        # Create a new child process using that command...
        self.create_child_process(cmd_list)
        # ...and set up the PipeReader objects to read from the child process
        #   STDOUT and STDERR
        if self.child_process is not None:
            self.stdout_reader.attach_fh(self.child_process.stdout)
            self.stderr_reader.attach_fh(self.child_process.stderr)

        # The first message in STDOUT should be the .m3u manifest
        self.m3u_waiting_flag = True

        # While downloading the media data object, update the callback function
        #   with the status of the current job
        while self.is_child_process_alive():

            # Pause a moment between each iteration of the loop (we don't want
            #   to hog system resources)
            time.sleep(self.longer_sleep_time)

            # Read from the child process STDOUT and STDERR, in the correct
            #   order, until there is nothing left to read
            while self.read_child_process():
                pass

            # !!! DEBUG: Any stall/timeout code goes here
            pass

        # Reset the child process, ready for the next one
        self.reset()

        # Check the .m3u manifest was fetched
        if self.m3u_manifest is None or self.m3u_manifest == '':

            msg = _('Failed to download the .m3u manifest')

            self.set_error(
                self.download_item_obj.media_data_obj,
                msg,
            )
            self.show_error(msg)

            self.set_return_code(self.ERROR)
            return

        # Prepare a system command to download the livestream using the .m3u
        #   manifest...
        cmd_list = [
            app_obj.ffmpeg_manager_obj.get_executable(),
            '-i',
            self.m3u_manifest,
            '-c',
            'copy',
            self.expect_output_path,
        ]

        # ...and display it in the Output tab and/or terminal, if required
        self.show_cmd(' '.join(cmd_list))

        # Create a new child process using that command...
        self.create_child_process(cmd_list)
        # ...and set up the PipeReader objects to read from the child process
        #   STDOUT and STDERR
        if self.child_process is not None:
            self.stdout_reader.attach_fh(self.child_process.stdout)
            self.stderr_reader.attach_fh(self.child_process.stderr)

        # !!! DEBUG: Because STDOUT/STDERR messages are missing, artificially
        # !!!   update the Progress List, as if the start of the download had
        # !!!   been detected (in self.read_child_process() code)
        self.set_actual_output_path(self.expect_output_path)

        # While downloading the media data object, update the callback function
        #   with the status of the current job
        while self.is_child_process_alive():

            # Pause a moment between each iteration of the loop (we don't want
            #   to hog system resources)
            time.sleep(self.sleep_time)

            # Read from the child process STDOUT and STDERR, in the correct
            #   order, until there is nothing left to read
            while self.read_child_process():
                pass

            # Check on our progress. As of v2.3.618, youtube-dl output on lines
            #   without a newline character cannot be retrieved by
            #   downloads.PipeReader; this is the next best thing
            if self.actual_output_path \
            and os.path.isfile(self.actual_output_path):

                current_size = os.path.getsize(self.actual_output_path)
                if current_size != self.output_size:

                    self.output_size = current_size
                    self.output_size_time = time.time()
                    self.segment_count += 1

                    # (Convert to, e.g. '27.5 MiB')
                    converted_size = ttutils.convert_bytes_to_string(
                        current_size,
                    )

                    self.download_data_callback('', str(converted_size))
                    self.show_msg(
                        ('Downloaded segment #{0}, size {1}').format(
                            self.segment_count,
                            converted_size,
                        ),
                    )

                    self.check_time = (app_obj.livestream_dl_timeout * 60) \
                    + time.time()

            # Perform a timeout, if necessary
            if self.check_time > 0 and self.check_time < time.time():

                # Halt the child process
                self.stop()
                self.show_msg('Download timed out')
                return


    def do_download_streamlink(self):

        """Called by self.do_download() when self.dl_mode is set to
        'streamlink'.

        Downloads a broadcasting livestream using streamlink.
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 9849 do_download_streamlink')

        # Import the main application (for convenience)
        app_obj = self.download_manager_obj.app_obj

        # Prepare a system command to download the livestream...
        cmd_list = ttutils.generate_streamlink_system_cmd(
            app_obj,
            self.download_item_obj.media_data_obj,
            self.expect_output_path,
        )

        # ...and display it in the Output tab and/or terminal, if required
        self.show_cmd(ttutils.prepare_system_cmd_for_display(cmd_list))

        # Create a new child process using that command...
        self.create_child_process(cmd_list)
        # ...and set up the PipeReader objects to read from the child process
        #   STDOUT and STDERR
        if self.child_process is not None:
            self.stdout_reader.attach_fh(self.child_process.stdout)
            self.stderr_reader.attach_fh(self.child_process.stderr)

        # While downloading the media data object, update the callback function
        #   with the status of the current job
        while self.is_child_process_alive():

            # Pause a moment between each iteration of the loop (we don't want
            #   to hog system resources)
            time.sleep(self.longer_sleep_time)

            # Read from the child process STDOUT and STDERR, in the correct
            #   order, until there is nothing left to read
            while self.read_child_process():
                pass

            # Check on our progress. As of v2.3.618, youtube-dl output on lines
            #   without a newline character cannot be retrieved by
            #   downloads.PipeReader; this is the next best thing
            if self.actual_output_path \
            and os.path.isfile(self.actual_output_path):

                current_size = os.path.getsize(self.actual_output_path)
                if current_size != self.output_size:

                    self.output_size = current_size
                    self.output_size_time = time.time()
                    self.segment_count += 1

                    # (Convert to, e.g. '27.5 MiB')
                    converted_size = ttutils.convert_bytes_to_string(
                        current_size,
                    )

                    self.download_data_callback('', str(converted_size))
                    self.show_msg(
                        ('Downloaded segment #{0}, size {1}').format(
                            self.segment_count,
                            converted_size,
                        ),
                    )

                    # Streamlink has been passed a --stream-timeout argument;
                    #   so add a few seconds to the usual timeout value, hoping
                    #   that streamlink's own timeout will happen first
                    self.check_time = (app_obj.livestream_dl_timeout * 60) \
                    + time.time() + 30

            # Perform a timeout, if necessary
            if self.check_time > 0 and self.check_time < time.time():

                # Halt the child process
                self.stop()
                self.show_msg('Download timed out')
                return


    def choose_path(self):

        """Called by self.__init__().

        When downloading from the Classic Mode tab, we don't know the video's
        name, so we have to choose an arbitrary one.

        Otherwise, the video's name (and file path) is already known, so we
        can just use the normal media.Video function to get it.

        Return values:

            The new value of self.expect_output_path

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 9943 choose_path')

        video_obj = self.download_item_obj.media_data_obj
        if not video_obj.dummy_flag:
            return video_obj.get_actual_path(self.download_manager_obj.app_obj)

        else:

            # Retrieve the user's preferred file extension
            file_ext = None
            if video_obj.dummy_format is not None:
                convert_flag, file_ext, resolution \
                = ttutils.extract_dummy_format(video_obj.dummy_format)

            if file_ext is None:
                file_ext = 'mp4'

            # Use an arbitrary filename in the form 'livestream_N.EXT'
            count = 0
            while 1:
                count += 1
                path = os.path.abspath(
                    os.path.join(
                        video_obj.dummy_dir, 'livestream_' + str(count) \
                        + '.' + file_ext,
                    ),
                )

                if not os.path.isfile(path):
                    return path


    def close(self):

        """Can be called by anything.

        Destructor function for this object.
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 9982 close')

        # Tell the PipeReader objects to shut down, thus joining their threads
        self.stdout_reader.join()
        self.stderr_reader.join()


    def create_child_process(self, cmd_list):

        """Called by self.do_download_basic(), .do_download_m3u() and
        .do_download_streamlink().

        Based on YoutubeDLDownloader._create_process().

        Executes the system command, creating a new child process which
        executes youtube-dl.

        Args:

            cmd_list (list): Python list that contains the command to execute

        Return values:

            True on success, False on an error

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 10010 create_child_process')

        # Strip double quotes from arguments
        # (Since we're sending the system command one argument at a time, we
        #   don't need to retain the double quotes around any single argument
        #   and, in fact, doing so would cause an error)
        cmd_list = ttutils.strip_double_quotes(cmd_list)

        # Create the child process
        info = preexec = None

        if os.name == 'nt':
            # Hide the child process window that MS Windows helpfully creates
            #   for us
            info = subprocess.STARTUPINFO()
            info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        else:
            # Make this child process the process group leader, so that we can
            #   later kill the whole process group with os.killpg
            preexec = os.setsid

        try:
            self.child_process = subprocess.Popen(
                cmd_list,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                preexec_fn=preexec,
                startupinfo=info,
            )

            return True

        except (ValueError, OSError) as error:
            # (Errors are expected and frequent)
            return False


    def download_data_callback(self, speed='', filesize=''):

        """Called by self.read_child_process() and .set_actual_output_path().

        Passes a dictionary of values to self.download_worker_obj so the main
        window can be updated.

        The dictionary is based on the one created by downloads.VideoDownloader
        (but with far fewer values included).

        This function is only called when a download is in progress;
        self.last_data_callback() is called at the end of it.
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 10062 download_data_callback')

        if self.segment_count == 0:
            percent = '?'
        else:
            percent = str(self.segment_count) + '/?'

        dl_stat_dict = {
            'status': formats.ACTIVE_STAGE_DOWNLOAD,
            'path': self.actual_output_dir,
            'filename': self.actual_output_filename,
            'extension': self.actual_output_ext,
            'percent': percent,
            'speed': speed,
            'filesize': filesize,
            'playlist_index': 1,
            'dl_sim_flag': False,
        }

        self.download_worker_obj.data_callback(dl_stat_dict)


    def is_child_process_alive(self):

        """Called by self.do_download_basic(), .do_download_m3u(),
        .do_download_streamlink() and .stop().

        Based on YoutubeDLDownloader._proc_is_alive().

        Called continuously during the self.do_fetch() loop to check whether
        the child process has finished or not.

        Return values:

            True if the child process is alive, otherwise returns False

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 10101 is_child_process_alive')

        if self.child_process is None:
            return False

        return self.child_process.poll() is None


    def last_data_callback(self):

        """Called by self.do_download().

        Based on YoutubeDLDownloader._last_data_hook().

        After the child process has finished, creates a new Python dictionary
        in the standard form described by
        downloads.VideoDownloader.extract_stdout_data().

        Sets key-value pairs in the dictonary, then passes it to the parent
        downloads.DownloadWorker object, confirming the result of the child
        process.

        The new key-value pairs are used to update the main window.
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 10127 last_data_callback')

        dl_stat_dict = {}

        if self.return_code == self.OK:
            dl_stat_dict['status'] = formats.COMPLETED_STAGE_FINISHED
        elif self.return_code == self.ERROR:
            dl_stat_dict['status'] = formats.MAIN_STAGE_ERROR
        elif self.return_code == self.STOPPED:
            dl_stat_dict['status'] = formats.ERROR_STAGE_STOPPED

        # Use some empty values in dl_stat_dict so that the Progress tab
        #   doesn't show arbitrary data from the most recent call to
        #   self.download_data_callback()
        dl_stat_dict['path'] = ''
        dl_stat_dict['filename'] = ''
        dl_stat_dict['extension'] = ''
        dl_stat_dict['percent'] = ''
        dl_stat_dict['speed'] = ''
        dl_stat_dict['filesize'] = ''
        dl_stat_dict['playlist_index'] = 1
        dl_stat_dict['dl_sim_flag'] = False

        # The True argument shows that this function is the caller
        self.download_worker_obj.data_callback(dl_stat_dict, True)


    def read_child_process(self):

        """Called by self.do_download_basic(), .do_download_m3u() and
        .do_download_streamlink().

        Reads from the child process STDOUT and STDERR, in the correct order.

        Return values:

            True if either STDOUT or STDERR were read. None if both queues were
                empty, or if STDERR was read and a network error was detected

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 10169 read_child_process')

        # mini_list is in the form [time, pipe_type, data]
        try:
            mini_list = self.queue.get_nowait()

        except:
            # Nothing left to read
            return None

        # Import the main application (for convenience)
        app_obj = self.download_manager_obj.app_obj

        # Failsafe check
        if not mini_list \
        or (mini_list[1] != 'stdout' and mini_list[1] != 'stderr'):

            # Just in case...
            GObject.timeout_add(
                0,
                self.download_manager_obj.app_obj.system_error,
                313,
                'Malformed STDOUT or STDERR data',
            )

        # STDOUT or STDERR has been read
        data = mini_list[2].rstrip()
        # On MS Windows we use cp1252, so that Tartube can communicate with the
        #   Windows console
        data = data.decode(ttutils.get_encoding(), 'replace')

        # STDOUT
        if mini_list[1] == 'stdout':

            if self.m3u_waiting_flag:

                # Assume the first line of text received in STDOUT is the .mu3
                #   manifest
                self.m3u_waiting_flag = False
                self.m3u_manifest = data
                # (The manifest will be visible in the next system command, so
                #   don't show it here)
                self.show_msg(
                    _(
                    'Downloaded the .m3u manifest, now downloading the' \
                    + ' livestream...'),
                )

                self.queue.task_done()
                return True

            # Capture the actual output path provided by the downloader
            if self.actual_output_path is None:

                output_path = None
                if self.dl_mode != 'streamlink':

                    match = re.search(
                        r'^\[download\] Destination\: (.*)\s*$',
                        data,
                    )
                    if match:
                        output_path = match.groups()[0]

                else:

                    if self.streamlink_start_flag == False \
                    and re.search(
                        r'^\[cli\]\[info\] Writing output to',
                        data,
                    ):
                        # Next line contains the output path
                        self.streamlink_start_flag = True

                    elif self.streamlink_start_flag == True:
                        # This line contains the output path
                        output_path = data
                        self.streamlink_start_flag = False

                if output_path:
                    self.set_actual_output_path(output_path)

            # Download updates in 'streamlink' download mode
            if self.dl_mode == 'streamlink':

                # !!! DEBUG This has not been tested, as the message is
                # !!!   currently not intercepted
                # e.g.
                # [download][output.mp4] Written 9.5 MB (36s @ 132.6 KB/s)
                match = re.search(
                    r'^\[download\]\[[^\[\]]+\] Written (.*) \(\S+ \@ (.*)\)',
                    data,
                )

                if match:
                    self.segment_count += 1

                    # Pass a dictionary of values to
                    #   self.download_worker_obj so the Progress List can be
                    #   updated
                    self.download_data_callback(
                        match.groups()[1],      # Bitrate
                        match.groups()[0],      # Filesize
                    )

            # Show output in the Output tab and/or terminal (if required)
            self.show_msg(data)

        # STDERR (downloads using youtube-dl, with or without .m3u; ignoring
        #   any empty error messages)
        elif data != '' and self.dl_mode != 'streamlink':

            mod_data = ttutils.stream_output_is_ignorable(data)
            if mod_data is not None:

                # Treat this as if it were a STDOUT message

                # Download updates in 'default' and 'default_m3u' download
                #   modes
                match = re.search(
                    r'^frame.*size\=\s*([\S]+).*bitrate\=\s*([\S]+)',
                    mod_data,
                )
                if match:
                    self.segment_count += 1

                    self.check_time = (app_obj.livestream_dl_timeout * 60) \
                    + time.time()

                    # Pass a dictionary of values to self.download_worker_obj
                    #   so the Progress List can be updated
                    self.download_data_callback(
                        match.groups()[1],      # Bitrate
                        match.groups()[0],      # Filesize
                    )

                # Show output in the Output tab and/or terminal (if required)
                self.show_msg(mod_data)

        # STDERR (downloads using youtube-dl/.m3u/FFmpeg, or using streamlink;
        #   ignoring any empty error messages)
        elif data != '':

            # Check for recognised errors/warnings, and update the appropriate
            #   media data object (immediately, if possible, or later
            #   otherwise)
            self.set_error(self.download_item_obj.media_data_obj, data)

            # Show output in the Output tab and/or terminal (if required)
            self.show_error(data)

            # (An error fetching the .m3u manifest is fatal)
            if self.m3u_waiting_flag:
                self.show_error(_('Failed to download the .m3u manifest'))
                self.set_return_code(self.ERROR)

        # Either (or both) of STDOUT and STDERR were non-empty
        self.queue.task_done()
        return True


    def reset(self):

        """Called by self.do_download_m3u().

        A modified version of self.close().

        The calling code uses two sub-processes, one after the other. This
        function is called when the first process is finished to reset
        everything, ready for the second function.
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 10342 reset')

        if self.child_process:

            # Tell the PipeReader objects to shut down, thus joining their
            #   threads
            self.stdout_reader.join()
            self.stderr_reader.join()

        self.child_process = None
        self.queue = queue.PriorityQueue()
        self.stdout_reader = PipeReader(self.queue, 'stdout')
        self.stderr_reader = PipeReader(self.queue, 'stderr')


    def set_actual_output_path(self, output_path):

        """Called by self.do_download_m3u() and .read_child_process().

        The downloader's output path is captured, meaning that the download has
        started.

        Updates IVs and the Progress List.

        Args:

            output_path (str): Full path to the downloader's output file

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 10373 set_actual_output_path')

        # Update IVs
        directory, filename, ext = ttutils.extract_path_components(output_path)

        self.actual_output_path = output_path
        self.actual_output_dir = directory
        self.actual_output_filename = filename
        self.actual_output_ext = ext

        # Pass a dictionary of values to self.download_worker_obj so the main
        #   window can be updated
        self.download_data_callback()


    def set_error(self, media_data_obj, msg):

        """Wrapper for media.Video.set_error().

        Args:

            media_data_obj (media.Video): The media data object to update. Only
                videos are updated by this function

            msg (str): The error message for this video

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 10402 set_error')

        if not self.first_error_flag:

            self.first_error_flag = True

            # The new error is the first error/warning generated during this
            #   operation; remove any errors/warnings from previous operations
            media_data_obj.reset_error_warning()

        # Set the new error
        media_data_obj.set_error(msg)


    def set_return_code(self, code):

        """Can be called by anything.

        Based on YoutubeDLDownloader._set_returncode().

        After the child process has terminated with an error of some kind,
        sets a new value for self.return_code, but only if the new return code
        is higher in the hierarchy of return codes than the current value.

        Args:

            code (int): A return code in the range 0-5

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 10433 set_return_code')

        if code >= self.return_code:
            self.return_code = code


    def show_cmd(self, cmd):

        """Can be called by anything.

        Shows a system command in the Output tab and/or terminal window, if
        required.

        Args:

            cmd (str): The system command to display

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 10453 show_cmd')

        # Import the main app (for convenience)
        app_obj = self.download_manager_obj.app_obj

        # Display the command in the Output tab, if allowed
        if app_obj.ytdl_output_system_cmd_flag:
            app_obj.main_win_obj.output_tab_write_system_cmd(
                self.download_worker_obj.worker_id,
                cmd,
            )

        # Display the message in the terminal, if allowed
        if app_obj.ytdl_write_system_cmd_flag:
            try:
                print(cmd)
            except:
                print('Command echoed in STDOUT with unprintable characters')

        # Display the message in the downloader log, if allowed
        if app_obj.ytdl_log_system_cmd_flag:
            app_obj.write_downloader_log(cmd)


    def show_msg(self, msg):

        """Can be called by anything.

        Shows a message in the Output tab and/or terminal window, if required.

        Args:

            msg (str): The message to display

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 10490 show_msg')

        # Import the main app (for convenience)
        app_obj = self.download_manager_obj.app_obj

        # Display the message in the Output tab, if allowed
        if app_obj.ytdl_output_stdout_flag:
            app_obj.main_win_obj.output_tab_write_stdout(
                self.download_worker_obj.worker_id,
                msg,
            )

        # Display the message in the terminal, if allowed
        if app_obj.ytdl_write_stdout_flag:
            # Git #175, Japanese text may produce a codec error here,
            #   despite the .decode() call above
            try:
                print(
                    msg.encode(ttutils.get_encoding(), 'replace'),
                )
            except:
                print('Message echoed in STDOUT with unprintable characters')

        # Write the message to the downloader log, if allowed
        if app_obj.ytdl_log_stdout_flag:
            app_obj.write_downloader_log(msg)


    def show_error(self, msg):

        """Can be called by anything.

        Shows an error message in the Output tab and/or terminal window, if
        required.

        Args:

            msg (str): The message to display

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 10532 show_error')

        # Import the main app (for convenience)
        app_obj = self.download_manager_obj.app_obj

        # Display the message in the Output tab, if allowed
        if app_obj.ytdl_output_stdout_flag:
            app_obj.main_win_obj.output_tab_write_stderr(
                self.download_worker_obj.worker_id,
                msg,
            )

        # Display the message in the terminal, if allowed
        if app_obj.ytdl_write_stderr_flag:
            # Git #175, Japanese text may produce a codec error here,
            #   despite the .decode() call above
            try:
                print(
                    msg.encode(ttutils.get_encoding(), 'replace'),
                )
            except:
                print('Message echoed in STDERR with unprintable characters')

        # Write the message to the downloader log (if required)
        if app_obj.ytdl_log_stderr_flag:
            app_obj.write_downloader_log(msg)


    def stop(self):

        """Called by DownloadWorker.close().

        Terminates the child process and sets this object's return code to
        self.STOPPED.
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 10569 stop')

        if self.is_child_process_alive():

            if os.name == 'nt':
                # os.killpg is not available on MS Windows (see
                #   https://bugs.python.org/issue5115 )
                self.child_process.kill()

                # When we kill the child process on MS Windows the return code
                #   gets set to 1, so we want to reset the return code back to
                #   0
                self.child_process.returncode = 0

            else:
                os.killpg(self.child_process.pid, signal.SIGKILL)

            self.set_return_code(self.STOPPED)


    def stop_soon(self):

        """Can be called by anything. Currently called by
        mainwin.MainWin.on_progress_list_stop_soon().

        StreamDownloader only downloads a single video, so we can ignore an
        instruction to stop after that download has finished.
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 10599 stop_soon')

        pass


class JSONFetcher(object):

    """Called by downloads.DownloadWorker.check_rss().

    Python class to download JSON data for a video which is believed to be a
    livestream, using youtube-dl.

    The video has been found in the channel's/playlist's RSS feed, but not by
    youtube-dl, when the channel/playlist was last checked downloaded.

    If the data can be downloaded, we assume that the livestream is currently
    broadcasting. If we get a 'This video is unavailable' error, we assume that
    the livestream is waiting to start.

    This is the behaviour exhibited on YouTube. It might work on other
    compatible websites, too, if the user has set manually set the URL for the
    channel/playlist RSS feed.

    This class creates a system child process and uses the child process to
    instruct youtube-dl to fetch the JSON data for the video.

    Reads from the child process STDOUT and STDERR, having set up a
    downloads.PipeReader object to do so in an asynchronous way.

    If one of the two outcomes described above takes place, the media.Video
    object's IVs are updated to mark it as a livestream.

    Args:

        download_manager_obj (downloads.DownloadManager): The download manager
            object handling the entire download operation

        download_worker_obj (downloads.DownloadWorker): The parent download
            worker object. The download manager uses multiple workers to
            implement simultaneous downloads. The download manager checks for
            free workers and, when it finds one, assigns it a
            download.DownloadItem object. When the worker is assigned a
            download item, it creates a new instance of this object for each
            detected livestream, and waits for this object to complete its
            task

        container_obj (media.Channel, media.Playlist): The channel/playlist
            in which a livestream has been detected

        entry_dict (dict): A dictionary of values generated when reading the
            RSS feed (provided by the Python feedparser module. The dictionary
            represents available data for a single livestream video

    Warnings:

        The calling function is responsible for calling the close() method
        when it's finished with this object, in order for this object to
        properly close down.

    """


    # Standard class methods


    def __init__(self, download_manager_obj, download_worker_obj, \
    container_obj, entry_dict):

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 10668 __init__')

        # IV list - class objects
        # -----------------------
        # The downloads.DownloadManager object handling the entire download
        #   operation
        self.download_manager_obj = download_manager_obj
        # The parent downloads.DownloadWorker object
        self.download_worker_obj = download_worker_obj
        # The media.Channel or media.Playlist object in which a livestream has
        #   been detected
        self.container_obj = container_obj

        # The child process created by self.create_child_process()
        self.child_process = None

        # Read from the child process STDOUT (i.e. self.child_process.stdout)
        #   and STDERR (i.e. self.child_process.stderr) in an asynchronous way
        #   by polling this queue.PriorityQueue object
        self.queue = queue.PriorityQueue()
        self.stdout_reader = PipeReader(self.queue, 'stdout')
        self.stderr_reader = PipeReader(self.queue, 'stderr')


        # IV list - other
        # ---------------
        # A dictionary of values generated when reading the RSS feed (provided
        #   by the Python feedparser module. The dictionary represents
        #   available data for a single livestream video
        self.entry_dict = entry_dict
        # Important data is extracted from the entry (below), and added to
        #   these IVs, ready for use
        self.video_name = None
        self.video_source = None
        self.video_descrip = None
        self.video_thumb_source = None
        self.video_upload_time = None

        # The time (in seconds) between iterations of the loop in
        #   self.do_fetch()
        self.sleep_time = 0.1


        # Code
        # ----
        # Initialise IVs from the RSS feed entry for the livestream video
        #   (saves a bit of time later)
        if 'title' in entry_dict:
            self.video_name = entry_dict['title']

        if 'link' in entry_dict:
            self.video_source = entry_dict['link']

        if 'summary' in entry_dict:
            self.video_descrip = entry_dict['summary']

        if 'media_thumbnail' in entry_dict \
        and entry_dict['media_thumbnail'] \
        and 'url' in entry_dict['media_thumbnail'][0]:
            self.video_thumb_source = entry_dict['media_thumbnail'][0]['url']

        if 'published_parsed' in entry_dict:

            try:
                # A time.struct_time object; convert to Unix time, to match
                #   media.Video.upload_time
                dt_obj = datetime.datetime.fromtimestamp(
                    time.mktime(entry_dict['published_parsed']),
                )

                self.video_upload_time = int(dt_obj.timestamp())

            except:
                self.video_upload_time = None


    # Public class methods


    def do_fetch(self):

        """Called by downloads.DownloadWorker.check_rss().

        Downloads JSON data for the livestream video whose URL is
        self.video_source.

        If the data can be downloaded, we assume that the livestream is
        currently broadcasting. If we get a 'This video is unavailable' error,
        we assume that the livestream is waiting to start.
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 10760 do_fetch')

        # Import the main app (for convenience)
        app_obj = self.download_manager_obj.app_obj

        # Convert a youtube-dl path beginning with ~ (not on MS Windows)
        #   (code copied from ttutils.generate_ytdl_system_cmd() )
        ytdl_path = app_obj.check_downloader(app_obj.ytdl_path)
        if os.name != 'nt':
            ytdl_path = re.sub(r'^\~', os.path.expanduser('~'), ytdl_path)

        # Generate the system command (but don't display it in the Output tab)
        if app_obj.ytdl_path_custom_flag:
            cmd_list = ['python3'] + [ytdl_path] + ['--dump-json'] \
            + [self.video_source]
        else:
            cmd_list = [ytdl_path] + ['--dump-json'] + [self.video_source]

        # Create a new child process using that command...
        self.create_child_process(cmd_list)
        # ...and set up the PipeReader objects to read from the child process'
        #   STDOUT and STDERR
        if self.child_process is not None:
            self.stdout_reader.attach_fh(self.child_process.stdout)
            self.stderr_reader.attach_fh(self.child_process.stderr)

        # Wait for the process to finish
        while self.is_child_process_alive():

            # Pause a moment between each iteration of the loop (we don't want
            #   to hog system resources)
            time.sleep(self.sleep_time)

        # Process has finished. Read from STDOUT and STDERR
        if self.read_child_process():

            # Download the video's thumbnail, if possible
            if self.video_thumb_source:

                # Get the thumbnail's extension...
                remote_file, remote_ext = os.path.splitext(
                    self.video_thumb_source,
                )

                # ...and thus get the filename used by youtube-dl when storing
                #   the thumbnail locally (assuming that the video's name, and
                #   the filename when it is later downloaded, are the same)
                local_thumb_path = os.path.abspath(
                    os.path.join(
                        self.container_obj.get_actual_dir(app_obj),
                        self.video_name + remote_ext,
                    ),
                )

                options_obj = self.download_worker_obj.options_manager_obj
                if not options_obj.options_dict['sim_keep_thumbnail']:
                    local_thumb_path = ttutils.convert_path_to_temp_dl_dir(
                        app_obj,
                        local_thumb_path,
                    )

                elif options_obj.options_dict['move_thumbnail']:
                    local_thumb_path = os.path.abspath(
                        os.path.join(
                            self.container_obj.get_actual_dir(app_obj),
                            app_obj.thumbs_sub_dir,
                            self.video_name + remote_ext,
                        )
                    )

                if local_thumb_path:
                    try:
                        request_obj = requests.get(
                            self.video_thumb_source,
                            timeout = app_obj.request_get_timeout,
                        )

                        with open(local_thumb_path, 'wb') as outfile:
                            outfile.write(request_obj.content)

                    except:
                        pass

                # Convert .webp thumbnails to .jpg, if required
                if local_thumb_path is not None \
                and not app_obj.ffmpeg_fail_flag \
                and app_obj.ffmpeg_convert_webp_flag \
                and not app_obj.ffmpeg_manager_obj.convert_webp(
                    local_thumb_path
                ):
                    app_obj.set_ffmpeg_fail_flag(True)
                    GObject.timeout_add(
                        0,
                        app_obj.system_error,
                        314,
                        app_obj.ffmpeg_fail_msg,
                    )


    def close(self):

        """Called by downloads.DownloadWorker.check_rss().

        Destructor function for this object.
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 10876 close')

        # Tell the PipeReader objects to shut down, thus joining their threads
        self.stdout_reader.join()
        self.stderr_reader.join()


    def create_child_process(self, cmd_list):

        """Called by self.do_fetch().

        Based on YoutubeDLDownloader._create_process().

        Executes the system command, creating a new child process which
        executes youtube-dl.

        Args:

            cmd_list (list): Python list that contains the command to execute

        Return values:

            True on success, False on an error

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 10894 create_child_process')

        # Strip double quotes from arguments
        # (Since we're sending the system command one argument at a time, we
        #   don't need to retain the double quotes around any single argument
        #   and, in fact, doing so would cause an error)
        cmd_list = ttutils.strip_double_quotes(cmd_list)

        # Create the child process
        info = preexec = None

        if os.name == 'nt':
            # Hide the child process window that MS Windows helpfully creates
            #   for us
            info = subprocess.STARTUPINFO()
            info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        else:
            # Make this child process the process group leader, so that we can
            #   later kill the whole process group with os.killpg
            preexec = os.setsid

        try:
            self.child_process = subprocess.Popen(
                cmd_list,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                preexec_fn=preexec,
                startupinfo=info,
            )

            return True

        except (ValueError, OSError) as error:
            # (Errors are expected and frequent)
            return False


    def is_child_process_alive(self):

        """Called by self.do_fetch() and self.stop().

        Based on YoutubeDLDownloader._proc_is_alive().

        Called continuously during the self.do_fetch() loop to check whether
        the child process has finished or not.

        Return values:

            True if the child process is alive, otherwise returns False.

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 10947 is_child_process_alive')

        if self.child_process is None:
            return False

        return self.child_process.poll() is None


    def read_child_process(self):

        """Called by self.do_fetch().

        Reads from the child process STDOUT and STDERR, in the correct order.

        For this JSONFetcher object, the order doesn't matter very much: we
        are expecting data in either STDOUT or STDERR.

        Return values:

            True if either STDOUT or STDERR were read, None if both queues were
                empty

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 10972 read_child_process')

        # mini_list is in the form [time, pipe_type, data]
        try:
            mini_list = self.queue.get_nowait()

        except:
            # Nothing left to read
            return None

        # Import the main application (for convenience)
        app_obj = self.download_manager_obj.app_obj

        # Failsafe check
        if not mini_list \
        or (mini_list[1] != 'stdout' and mini_list[1] != 'stderr'):

            # Just in case...
            GObject.timeout_add(
                0,
                self.download_manager_obj.app_obj.system_error,
                315,
                'Malformed STDOUT or STDERR data',
            )

        # STDOUT or STDERR has been read
        data = mini_list[2].rstrip()
        # Convert bytes to string
        data = data.decode(ttutils.get_encoding(), 'replace')

        # STDOUT
        if mini_list[1] == 'stdout':

            if data[:1] == '{':

                # Broadcasting livestream detected; create a new media.Video
                #   object
                GObject.timeout_add(
                    0,
                    app_obj.create_livestream_from_download,
                    self.container_obj,
                    2,                      # Livestream has started
                    self.video_name,
                    self.video_source,
                    self.video_descrip,
                    self.video_upload_time,
                )

        # STDERR (ignoring any empty error messages)
        elif data != '':

            live_data_dict = ttutils.extract_livestream_data(data)
            if live_data_dict:

                # Waiting livestream detected; create a new media.Video object
                GObject.timeout_add(
                    0,
                    app_obj.create_livestream_from_download,
                    self.container_obj,
                    1,                  # Livestream waiting to start
                    self.video_name,
                    self.video_source,
                    self.video_descrip,
                    self.video_upload_time,
                    live_data_dict,
                )

        # Either (or both) of STDOUT and STDERR were non-empty
        self.queue.task_done()
        return True


    def stop(self):

        """Called by DownloadWorker.close().

        Terminates the child process.
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 11052 stop')

        if self.is_child_process_alive():

            if os.name == 'nt':
                # os.killpg is not available on MS Windows (see
                #   https://bugs.python.org/issue5115 )
                self.child_process.kill()

                # When we kill the child process on MS Windows the return code
                #   gets set to 1, so we want to reset the return code back to
                #   0
                self.child_process.returncode = 0

            else:
                os.killpg(self.child_process.pid, signal.SIGKILL)


class StreamManager(threading.Thread):

    """Called by mainapp.TartubeApp.livestream_manager_start().

    Python class to create a system child process, to check media.Video objects
    already marked as livestreams, to see whether they have started or stopped
    broadcasting.

    Reads from the child process STDOUT and STDERR, having set up a
    downloads.PipeReader object to do so in an asynchronous way.

    Args:

        app_obj (mainapp.TartubeApp): The main application

    """


    # Standard class methods


    def __init__(self, app_obj):

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 11094 __init__')

        super(StreamManager, self).__init__()

        # IV list - class objects
        # -----------------------
        # The mainapp.TartubeApp object
        self.app_obj = app_obj
        # The downloads.MiniJSONFetcher object used to check each media.Video
        #   object marked as a livestream
        self.mini_fetcher_obj = None


        # IV list - other
        # ---------------
        # A local list of media.Video objects marked as livestreams (in case
        #   the mainapp.TartubeApp IV changes during the course of this
        #   operation)
        # Dictionary in the form:
        #   key = media data object's unique .dbid
        #   value = the media data object itself
        self.video_dict = {}

        # Flag set to False if self.stop_livestream_operation() is called
        # The False value halts the loop in self.run()
        self.running_flag = True

        # Code
        # ----

        # Let's get this party started!
        self.start()


    # Public class methods


    def run(self):

        """Called as a result of self.__init__().

        Initiates the download.
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 11139 run')

        # Generate a local list of media.Video objects marked as livestreams
        #   (in case the mainapp.TartubeApp IV changes during the course of
        #   this operation)
        self.video_dict = self.app_obj.media_reg_live_dict.copy()

        for video_obj in self.video_dict.values():

            if not self.running_flag:
                break

            # For each media.Video in turn, try to fetch JSON data
            # If the data is received, assume the livestream is live. If a
            #   'This video is unavailable' error is received, the livestream
            #   is waiting to go live
            self.mini_fetcher_obj = MiniJSONFetcher(self, video_obj)

            # Then execute the assigned job
            self.mini_fetcher_obj.do_fetch()

            # Call the destructor function of the MiniJSONFetcher object
            #   (first checking it still exists, in case
            #   self.stop_livestream_operation() has been called)
            if self.mini_fetcher_obj:
                self.mini_fetcher_obj.close()
                self.mini_fetcher_obj = None

        # Operation complete. If self.stop_livestream_operation() was called,
        #   then the mainapp.TartubeApp function has already been called
        if self.running_flag:
            self.running_flag = False
            GObject.timeout_add(
                0,
                self.app_obj.livestream_manager_finished,
            )


    def stop_livestream_operation(self):

        """Can be called by anything.

        Based on downloads.DownloadManager.stop_downloads().

        Stops the livestream operation. On the next iteration of self.run()'s
        loop, the downloads.MiniJSONFetcher objects are cleaned up.
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 11185 stop_livestream_operation')

        self.running_flag = False

        # Halt the MiniJSONFetcher; it doesn't matter if it was in the middle
        #   of doing something
        if self.mini_fetcher_obj:
            self.mini_fetcher_obj.close()
            self.mini_fetcher_obj = None

        # Call the mainapp.TartubeApp function to update everything (it's not
        #   called from self.run(), in this situation)
        GObject.timeout_add(
            0,
            self.app_obj.livestream_manager_finished,
        )


class MiniJSONFetcher(object):

    """Called by downloads.StreamManager.run().

    A modified version of downloads.JSONFetcher (the former is called by
    downloads.DownloadWorker only; using a second Python class for the same
    objective makes the code somewhat simpler).

    Python class to fetch JSON data for a livestream video, using youtube-dl.

    Creates a system child process and uses the child process to instruct
    youtube-dl to fetch the JSON data for the video.

    Reads from the child process STDOUT and STDERR, having set up a
    downloads.PipeReader object to do so in an asynchronous way.

    Args:

        livestream_manager_obj (downloads.StreamManager): The livestream
            manager object handling the entire livestream operation

        video_obj (media.Video): The livestream video whose JSON data should be
            fetched (the equivalent of right-clicking the video in the Video
            Catalogue, and selecting 'Check this video')

    """


    # Standard class methods


    def __init__(self, livestream_manager_obj, video_obj):

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 11234 __init__')

        # IV list - class objects
        # -----------------------
        # The downloads.StreamManager object handling the entire livestream
        #   operation
        self.livestream_manager_obj = livestream_manager_obj
        # The media.Video object for which new JSON data must be fetched
        #   (the equivalent of right-clicking the video in the Video Catalogue,
        #   and selecting 'Check this video')
        self.video_obj = video_obj

        # The child process created by self.create_child_process()
        self.child_process = None

        # Read from the child process STDOUT (i.e. self.child_process.stdout)
        #   and STDERR (i.e. self.child_process.stderr) in an asynchronous way
        #   by polling this queue.PriorityQueue object
        self.queue = queue.PriorityQueue()
        self.stdout_reader = PipeReader(self.queue, 'stdout')
        self.stderr_reader = PipeReader(self.queue, 'stderr')


        # IV list - other
        # ---------------
        # The time (in seconds) between iterations of the loop in
        #   self.do_fetch()
        self.sleep_time = 0.1


    # Public class methods


    def do_fetch(self):

        """Called by downloads.StreamManager.run().

        Downloads JSON data for the livestream video, self.video_obj.

        If the data can be downloaded, we assume that the livestream is
        currently broadcasting. If we get a 'This video is unavailable' error,
        we assume that the livestream is waiting to start.
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 11279 do_fetch')

        # Import the main app (for convenience)
        app_obj = self.livestream_manager_obj.app_obj

        # Convert a youtube-dl path beginning with ~ (not on MS Windows)
        #   (code copied from ttutils.generate_ytdl_system_cmd() )
        ytdl_path = app_obj.check_downloader(app_obj.ytdl_path)
        if os.name != 'nt':
            ytdl_path = re.sub(r'^\~', os.path.expanduser('~'), ytdl_path)

        # Generate the system command
        if app_obj.ytdl_path_custom_flag:
            cmd_list = ['python3'] + [ytdl_path] + ['--dump-json'] \
            + [self.video_obj.source]
        else:
            cmd_list = [ytdl_path] + ['--dump-json'] + [self.video_obj.source]

        # Create a new child process using that command...
        self.create_child_process(cmd_list)
        # ...and set up the PipeReader objects to read from the child process
        #   STDOUT and STDERR
        if self.child_process is not None:
            self.stdout_reader.attach_fh(self.child_process.stdout)
            self.stderr_reader.attach_fh(self.child_process.stderr)

        # Wait for the process to finish
        while self.is_child_process_alive():

            # Pause a moment between each iteration of the loop (we don't want
            #   to hog system resources)
            time.sleep(self.sleep_time)

            # Read from the child process STDOUT and STDERR, in the correct
            #   order, until there is nothing left to read
            while self.read_child_process():
                pass


    def close(self):

        """Called by downloads.StreamManager.run().

        Destructor function for this object.
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 11326 close')

        # Tell the PipeReader objects to shut down, thus joining their threads
        self.stdout_reader.join()
        self.stderr_reader.join()


    def create_child_process(self, cmd_list):

        """Called by self.do_fetch().

        Based on YoutubeDLDownloader._create_process().

        Executes the system command, creating a new child process which
        executes youtube-dl.

        Args:

            cmd_list (list): Python list that contains the command to execute

        Return values:

            True on success, False on an error

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 11353 create_child_process')

        # Strip double quotes from arguments
        # (Since we're sending the system command one argument at a time, we
        #   don't need to retain the double quotes around any single argument
        #   and, in fact, doing so would cause an error)
        cmd_list = ttutils.strip_double_quotes(cmd_list)

        # Create the child process
        info = preexec = None

        if os.name == 'nt':
            # Hide the child process window that MS Windows helpfully creates
            #   for us
            info = subprocess.STARTUPINFO()
            info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        else:
            # Make this child process the process group leader, so that we can
            #   later kill the whole process group with os.killpg
            preexec = os.setsid

        try:
            self.child_process = subprocess.Popen(
                cmd_list,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                preexec_fn=preexec,
                startupinfo=info,
            )

            return True

        except (ValueError, OSError) as error:
            # (Errors are expected and frequent)
            return False


    def is_child_process_alive(self):

        """Called by self.do_fetch() and self.stop().

        Based on YoutubeDLDownloader._proc_is_alive().

        Called continuously during the self.do_fetch() loop to check whether
        the child process has finished or not.

        Return values:

            True if the child process is alive, otherwise returns False

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 11406 is_child_process_alive')

        if self.child_process is None:
            return False

        return self.child_process.poll() is None


    def parse_json(self, stdout):

        """Called by self.do_fetch().

        Code copied from downloads.VideoDownloader.extract_stdout_data().

        Converts the receivd JSON data into a dictionary, and returns the
        dictionary.

        Args:

            stdout (str): A string of JSON data as it was received from
                youtube-dl (and starting with the character { )

        Return values:

            The JSON data, converted into a Python dictionary

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 11435 parse_json')

        # (Try/except to check for invalid JSON)
        try:
            return json.loads(stdout)

        except:
            GObject.timeout_add(
                0,
                app_obj.system_error,
                316,
                'Invalid JSON data received from server',
            )

            return {}


    def read_child_process(self):

        """Called by self.do_fetch().

        Reads from the child process STDOUT and STDERR, in the correct order.

        Return values:

            True if either STDOUT or STDERR were read, None if both queues were
                empty

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 11466 read_child_process')

        # mini_list is in the form [time, pipe_type, data]
        try:
            mini_list = self.queue.get_nowait()

        except:
            # Nothing left to read
            return None

        # Import the main application (for convenience)
        app_obj = self.livestream_manager_obj.app_obj

        # Failsafe check
        if not mini_list \
        or (mini_list[1] != 'stdout' and mini_list[1] != 'stderr'):

            # Just in case...
            GObject.timeout_add(
                0,
                self.download_manager_obj.app_obj.system_error,
                317,
                'Malformed STDOUT or STDERR data',
            )

        # STDOUT or STDERR has been read
        data = mini_list[2].rstrip()
        # Convert bytes to string
        data = data.decode(ttutils.get_encoding(), 'replace')

        # STDOUT
        if mini_list[1] == 'stdout':

            if data[:1] == '{':

                # Broadcasting livestream detected
                json_dict = self.parse_json(data)
                if self.video_obj.live_mode == 1:

                    # Waiting livestream has gone live
                    GObject.timeout_add(
                        0,
                        app_obj.mark_video_live,
                        self.video_obj,
                        2,              # Livestream is broadcasting
                        {},             # No livestream data
                        True,           # Don't update Video Index yet
                        True,           # Don't update Video Catalogue yet
                    )

                elif self.video_obj.live_mode == 2 \
                and (not 'is_live' in json_dict or not json_dict['is_live']):

                    # Broadcasting livestream has finished
                    GObject.timeout_add(
                        0,
                        app_obj.mark_video_live,
                        self.video_obj,
                        0,                  # Livestream has finished
                        {},             # Reset any livestream data
                        None,           # Reset any l/s server messages
                        True,           # Don't update Video Index yet
                        True,           # Don't update Video Catalogue yet
                    )

                # The video's name and description might change during the
                #   livestream; update them, if so
                if 'title' in json_dict:
                    self.video_obj.set_nickname(json_dict['title'])

                if 'id' in json_dict:
                    self.video_obj.set_vid(json_dict['id'])

                if 'description' in json_dict:
                    self.video_obj.set_video_descrip(
                        app_obj,
                        json_dict['description'],
                        app_obj.main_win_obj.descrip_line_max_len,
                    )

        # STDERR (ignoring any empty error messages)
        elif data != '':

            # (v2.2.100: In approximately October 2020, YouTube started using a
            #   new error message for livestreams waiting to start)
            if self.video_obj.live_mode == 1:

                live_data_dict = ttutils.extract_livestream_data(data)
                if live_data_dict:
                    self.video_obj.set_live_data(live_data_dict)

            elif self.video_obj.live_mode == 2 \
            and re.search('This video is unavailable', data):

                # The livestream broadcast has been deleted by its owner (or is
                #   not available on the website, possibly temporarily)
                app_obj.add_media_reg_live_vanished_dict(self.video_obj),

        # Either (or both) of STDOUT and STDERR were non-empty
        self.queue.task_done()
        return True


    def stop(self):

        """Called by DownloadWorker.close().

        Terminates the child process.
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 11577 stop')

        if self.is_child_process_alive():

            if os.name == 'nt':
                # os.killpg is not available on MS Windows (see
                #   https://bugs.python.org/issue5115 )
                self.child_process.kill()

                # When we kill the child process on MS Windows the return code
                #   gets set to 1, so we want to reset the return code back to
                #   0
                self.child_process.returncode = 0

            else:
                os.killpg(self.child_process.pid, signal.SIGKILL)


class CustomDLManager(object):

    """Called by mainapp.TartubeApp.create_custom_dl_manager().

    Python class to store settings for a custom download. The user can create
    as many instances of this object as they like, and can launch a custom
    download using settings from any of them.

    Args:

        uid (int): Unique ID for this custom download manager (unique only to
            this class of objects)

        name (str): Non-unique name forthis custom download manager

    """


    # Standard class methods


    def __init__(self, uid, name):

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 11619 __init__')

        # IV list - other
        # ---------------
        # Unique ID for this custom download manager
        self.uid = uid
        # A non-unique name for this custom download manager
        self.name = name

        # If True, during a custom download, download every video which is
        #   marked as not downloaded (often after clicking the 'Check all'
        #   button); don't download channels/playlists directly
        self.dl_by_video_flag = False
        # If True, during a custom download, perform a simulated download first
        #   (as happens by default in custom downloads launched from the
        #   Classic Mode tab). Ignored if self.dl_by_video_flag is False
        self.dl_precede_flag = False

        # If True, during a custom download, only download the video if
        #   subtitles are available for it. Ignored if self.dl_precede_flag is
        #   False
        self.dl_if_subs_flag = False
        # If set, during the checking stage of a custom download, don't add
        #   (checked) videos to Tartube's database. Ignored if
        #   self.dl_if_subs_flag is False
        self.ignore_if_no_subs_flag = False
        # If set, during a custom download, only download the video if
        #   subtitles in any of these formats are available for it. Each item
        #   in the list is a value in formats.LANGUAGE_CODE_DICT (e.g. 'en',
        #   'live_chat'). Ignored if self.dl_if_subs_flag is False
        self.dl_if_subs_list = []

        # If True, during a custom download, split a video into video clips
        #   using its timestamps. Ignored if self.dl_by_video_flag is False
        # Note that IVs for splitting videos (e.g.
        #   mainapp.TartubeApp.split_video_name_mode) apply in this situation
        #   as well
        self.split_flag = False
        # If True, during a custom download, video slices identified by
        #   SponsorBlock are removed. Ignored if self.dl_by_video_flag is
        #   False, or if self.split_flag is True
        self.slice_flag = False
        # A dictionary specifying which categories of video slice should be
        #   removed. Keys are SponsorBlock categories; values are True to
        #   remove the slice, False to retain it
        # NB A sorted list of keys from this dictionary appears in
        #   formats.SPONSORBLOCK_CATEGORY_LIST
        self.slice_dict = {
            'sponsor': True,
            'selfpromo': False,
            'interaction': False,
            'intro': False,
            'outro': False,
            'preview': False,
            'music_offtopic': False,
        }
        # If True, during a custom download, a delay (in minutes) is applied
        #   between media data object downloads. When applied to a
        #   channel/playlist, the delay occurs after the whole channel/
        #   playlist. When applied directly to videos, the delay occurs after
        #   each video
        # NB The delay is applied during real downloads, but not during
        #   simulated downloads (operation types 'custom_sim' or 'classic_sim')
        self.delay_flag = False
        # The maximum delay to apply (in minutes, minimum value 0.2). Ignored
        #   if self.delay_flag is False
        self.delay_max = 5
        # The minimum delay to apply (in minutes, minimum value 0, maximum
        #   value self.delay_max). If specified, the delay is a random length
        #   of time between this value and self.delay_max. Ignored if
        #   self.delay_flag is False
        self.delay_min = 0

        # During a custom download, any videos whose source URL is YouTube can
        #   be diverted to another website. This IV uses the values:
        #       'default' - Use the original YouTube URL
        #       'hooktube' - Divert to hooktube.com
        #       'invidious' - Divert to invidio.us
        #       'other' - user enters their own alternative front-end website
        self.divert_mode = 'default'
        # If self.divert_mode is 'other', the address of the YouTube
        #   alternative. The string directly replaces the 'youtube.com' part of
        #   a URL; so the string must be something like 'hooktube.com' not
        #   'http://hooktube.com' or anything like that
        # Ignored if it does not contain at least 3 characters. Ignored for any
        #   other value of self.divert_mode
        self.divert_website = ''

        # If True, don't download broadcasting livestreams. Ignored if
        #   self.dl_by_video_flag is False
        self.ignore_stream_flag = False
        # If True, don't download finished livestreams. Ignored if
        #   self.dl_by_video_flag is False
        self.ignore_old_stream_flag = False
        # If True, only download broadcasting livestreams. Ignored if
        #   self.dl_by_video_flag is False. Mutually incompatible with
        #   self.ignore_stream_flag
        self.dl_if_stream_flag = False
        # If True, only download finished livestreams. Ignored if
        #   self.dl_by_video_flag is False. Mutually incompatible with
        #   self.ignore_old_stream_flag
        self.dl_if_old_stream_flag = False


    # Public class methods


    def clone_settings(self, other_obj):

        """Called by mainapp.TartubeApp.clone_custom_dl_manager_from_window().

        Clones custom download settings from the specified object into this
        object, completely replacing this object's settings.

        Args:

            other_obj (downloads.CustomDLManager): The custom download manager
                object (usually the current one), from which settings will be
                cloned

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 11742 clone_settings')

        self.dl_by_video_flag = other_obj.dl_by_video_flag
        self.dl_if_subs_flag = other_obj.dl_if_subs_flag
        self.ignore_if_no_subs_flag = other_obj.ignore_if_no_subs_flag
        self.dl_if_subs_list = other_obj.dl_if_subs_list
        self.split_flag = other_obj.split_flag
        self.slice_flag = other_obj.slice_flag
        self.slice_dict = other_obj.slice_dict.copy()
        self.divert_mode = other_obj.divert_mode
        self.divert_website = other_obj.divert_website
        self.delay_flag = other_obj.delay_flag
        self.delay_min = other_obj.delay_min


    def reset_settings(self):

        """Currently not called by anything (but might be needed in the
        future).

        Resets settings to their default values.
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 11766 reset_settings')

        self.dl_by_video_flag = False
        self.dl_if_subs_flag = False
        self.ignore_if_no_subs_flag = False
        self.dl_if_subs_list = []
        self.split_flag = False
        self.slice_flag = False
        self.slice_dict = {
            'sponsor': True,
            'selfpromo': False,
            'interaction': False,
            'intro': False,
            'outro': False,
            'preview': False,
            'music_offtopic': False,
        }
        self.divert_mode = 'default'
        self.divert_website = ''
        self.delay_flag = False
        self.delay_max = 5
        self.delay_min = 0


    def set_dl_precede_flag(self, flag):

        """Can be called by anything. Mostly called by
        mainapp.TartubeApp.start() and .set_dl_precede_flag().

        Updates the IV.

        Args:

            flag (bool): The new value of the IV

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 11804 set_dl_precede_flag')

        if not flag:
            self.dl_precede_flag = False
        else:
            self.dl_by_video_flag = True
            self.dl_precede_flag = True


class PipeReader(threading.Thread):

    """Called by downloads.VideoDownloader.__init__().

    Based on the PipeReader class in youtube-dl-gui.

    Python class used by downloads.VideoDownloader, downloads.ClipDownloader,
    downloads.StreamDownloader, downloads.JSONFetcher,
    downloads.MiniJSONFetcher, info.InfoManager and updates.UpdateManager,
    to avoid deadlocks when reading from child process pipes STDOUT and STDERR.

    This class uses python threads and queues in order to read from child
    process pipes in an asynchronous way.

    Args:

        queue (queue.PriorityQueue): Python queue to store the output of the
            child process

        pipe_type (str): This object reads from either 'stdout' or 'stderr'

    Warnings:

        All the actions are based on 'str' types. The calling function must
        convert the queued items back to 'unicode', if necessary

    """


    # Standard class methods


    def __init__(self, queue, pipe_type):

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 11848 __init__')

        super(PipeReader, self).__init__()

        # IV list - other
        # ---------------
        # Python queue.PriorityQueue to store the output of the child process
        self.queue = queue
        # This object reads from either 'stdout' or 'stderr'
        self.pipe_type = pipe_type

        # The time (in seconds) between iterations of the loop in self.run()
        # Without some kind of delay, the GUI interface becomes sluggish. The
        #   length of the delay doesn't matter, so make it as short as
        #   reasonably possible
        self.sleep_time = 0.001
        # Flag that is set to False by self.join(), which enables the loop in
        #   self.run() to terminate
        self.running_flag = True
        # Set by self.attach_fh(). The filehandle for the child process STDOUT
        #   or STDERR, e.g. downloads.VideoDownloader.child_process.stdout
        self.fh = None


        # Code
        # ----

        # Let's get this party started!
        self.start()


    # Public class methods


    def run(self):

        """Called as a result of self.__init__().

        Reads from STDOUT or STERR using the attached filed filehandle.
        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 11890 run')

        # Use this flag so that the loop can ignore FFmpeg error messsages
        #   (because the parent VideoDownloader object shouldn't use that as a
        #   serious error)
        ignore_line = False

        while self.running_flag:

            if self.fh is not None:

                # Read the filehandle until the sentinel line (matching '') is
                #   found, marking the end of the file; see
                #   https://stackoverflow.com/questions/52446415/
                #   line-in-iterfp-readline-rather-than-line-in-fp
                for line in iter(self.fh.readline, str('')):

                    if line == b'':
                        # End of file
                        break

                    if str.encode('ffmpeg version') in line:
                        ignore_line = True

                    if not ignore_line:

                        # Add a tuple to the queue.PriorityQueue. The queue's
                        #   entries are sorted by the first item of the tuple,
                        #   so the queue is read in the correct order
                        self.queue.put_nowait(
                            [time.time(), self.pipe_type, line],
                        )

                self.fh = None
                ignore_line = False

            # This delay is required; see the comments in self.__init__()
            time.sleep(self.sleep_time)


    def attach_fh(self, fh):

        """Called by downloads.VideoDownloader.do_download() and comparable
        functions.

        Sets the filehandle for the child process STDOUT or STDERR, e.g.
        downloads.VideoDownloader.child_process.stdout

        Args:

            fh (filehandle): The open filehandle for STDOUT or STDERR

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 11945 attach_fh')

        self.fh = fh


    def join(self, timeout=None):

        """Called by downloads.VideoDownloader.close(), which is the destructor
        function for that object.

        Join the thread and update IVs.

        Args:

            timeout (-): No calling code sets a timeout

        """

        if DEBUG_FUNC_FLAG:
            ttutils.debug_time('dld 11964 join')

        self.running_flag = False
        super(PipeReader, self).join(timeout)
