$ set(CMAKE_MSVC_RUNTIME_LIBRARY MultiThreadedDLL)

$ pulseaudio --version
$ sudo apt-get install pulseaudio
$ pulseaudio

# auto conference_service = sdk->media_io();

# auto session_service = sdk->session();
$ auto conference_service = sdk->conference();

// Wait device to be set
wait(sdk->device_management().set_preferred_input_audio_device(device));

// Invoking the method directly requires chaining successive operations
// via the `then` call
sdk->device_management().set_preferred_input_audio_device(device)
  .then([]() {
    // device is now set
  })
  .on_error([](auto&& e) {
    // Handle exception
  });
// Wait device to be set
wait(sdk->device_management().set_preferred_input_audio_device(device));

// Invoking the method directly requires chaining successive operations
// via the `then` call
sdk->device_management().set_preferred_input_audio_device(device)
  .then([]() {
    // device is now set
  })
  .on_error([](auto&& e) {
    // Handle exception
  });
// Wait for the conference creation
auto conf_info = wait(sdk->conference().join(conf_options, join_options));

 // Invoking the method directly requires chaining successive operations
 // via the `then` call
sdk->conference().join(conf_options, join_options))
   .then[](auto&& info) {
     // Do something with the returned conf info;
   })
   .on_error([](auto&& e) {
     // Handle exception
   });
// Invoke the method via wait blocks until the method succeeds or fails
wait(sdk->conference().listen(conf, join));

// Invoking the method directly requires chaining successive operations
// via the `then` call
sdk->conference().listen(conf, join)
  .then([](conference_info&&) {
    // The user joined the conference
  })
  .on_error([](auto&& e) {
    // Handle exception
  });
  // Invoke the method via wait blocks until the method succeeds or fails
wait(sdk->conference().leave());

// Invoking the method directly requires chaining successive operations
// via the `then` call
sdk->conference().leave()
  .then([]() {
    // The user left the conference
  })
  .on_error([](auto&& e) {
    // Handle exception
  });
  // Invoke the method via wait blocks until the method succeeds or fails
wait(sdk->conference().send("some message", std::move(participant_ids)));

// Invoking the method directly requires chaining successive operations
// via the `then` call
 sdk->conference().send("some message", std::move(participant_ids))
 .then([]() {
    // The message was sent
 })
 .on_error([](auto&& e){
    // Rethrow and handle the exception
 });
 // Invoke the method via wait blocks until the method succeeds or fails
wait(sdk->conference().mute(true));

// Invoking the method directly requires chaining successive operations
// via the `then` call
 sdk->conference().mute(true)
 .then([]() {
    // The microphone is now muted
 })
 .on_error([](auto&& e){
    // The operation failed, and microphone is not muted
 });
 // Invoke the method via wait blocks until the method succeeds or fails
wait(sdk->conference().remote_mute(true, participant_id));

// Invoking the method directly requires chaining successive operations
// via the `then` call
 sdk->conference().remote_mute(true, participant_id)
 .then([]() {
    // The remote participant is now muted
 })
 .on_error([](auto&& e){
    // The operation failed, and remote participant is not muted
 });
 
