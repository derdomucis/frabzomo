$ cd sdk-release/share/dolbyio/comms/sample/
$ mkdir build
$ cd build/ && cmake ../
$ cmake --build . -j 8
        [  4%] Building CXX object custom_recorder/CMakeFiles/custom_recorder.dir/custom_recorder.cc.o
        [ 13%] Building CXX object media_source/CMakeFiles/media_source_file.dir/file/source_capture.cc.o
        [ 21%] Building CXX object custom_injector/CMakeFiles/custom_injector.dir/custom_injector.cc.o
        [ 21%] Building CXX object custom_video_processor/CMakeFiles/custom_video_processor.dir/custom_video_processor.cc.o
        [ 30%] Building CXX object media_source/CMakeFiles/media_source_file.dir/file/utils/audio_buffer.cc.o
        [ 30%] Building CXX object media_source/CMakeFiles/media_source_file.dir/file/libav_wrapper/avcontext.cc.o
        [ 30%] Building CXX object media_source/CMakeFiles/media_source_file.dir/file/libav_wrapper/decoder.cc.o
        [ 34%] Building CXX object media_source/CMakeFiles/media_source_file.dir/file/libav_wrapper/frame.cc.o
        [ 39%] Building CXX object media_source/CMakeFiles/media_source_file.dir/file/utils/media_frame.cc.o
        [ 43%] Linking CXX static library libcustom_injector.a
        [ 43%] Built target custom_injector
        [ 52%] Linking CXX static library libmedia_source_file.a
        [ 52%] Linking CXX static library libcustom_recorder.a
        [ 56%] Built target custom_recorder
        [ 56%] Built target media_source_file
        [ 56%] Built target custom_video_processor
        [ 65%] Building CXX object utilities/CMakeFiles/utils.dir/sdk/interactions.cc.o
        [ 69%] Building CXX object utilities/CMakeFiles/utils.dir/sdk/events.cc.o
        [ 78%] Building CXX object utilities/CMakeFiles/utils.dir/commands_handler.cc.o
        [ 82%] Building CXX object utilities/CMakeFiles/utils.dir/ui_loop/ui.cc.o
        [ 86%] Building CXX object utilities/CMakeFiles/utils.dir/ui_loop/macos_ui.mm.o
        [ 86%] Building CXX object utilities/CMakeFiles/utils.dir/media/media_io_interactions.cc.o
        [ 86%] Building CXX object utilities/CMakeFiles/utils.dir/sdk/device_manager/interactions.cc.o
        [ 91%] Linking CXX static library libutils.a
        [ 91%] Built target utils
        [ 95%] Building CXX object desktop_app/CMakeFiles/desktop_app.dir/desktop_app.cc.o
        [100%] Linking CXX executable desktop_app
        [100%] Built target desktop_app




$ ./desktop_app -u USERNAME -k ACCESS_TOKEN -i CONF_ID -l LOG_LEVEL -ml LOG_LEVEL_MEDIA -p user -m AV -spatial shared

                 or

$ ./desktop_app -u USERNAME -k ACCESS_TOKEN -i CONF_ID -l LOG_LEVEL -ml LOG_LEVEL_MEDIA -p user -enable-media-io -d PATH_TO_DUMP_DIRECTORY -m AV -f SOME_FILE.mp4 -spatial shared

sdk->audio().local()
.start_()
.then([injection_src]() {
  std::cerr << "start audio success" << std::endl;
  if (injection_src)
    injection_src->set_audio_capture(true);
})
.on_error([](std::exception_ptr&& e) {
  try {
    std::rethrow_exception(e);
  } catch (std::exception& e) {
    std::cerr << "start audio failed: " << e.what() << std::endl;
  }
});




