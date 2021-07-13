// get the button element
let button_turquoise = document.getElementById( 'button-turquise' );

// LED ist am Anfang aus
let button_turquoise_state = false;


// check für aktive Verbindungen hmhm
let isConnectionActive = false;

// Verbindung mit dem websocket server
let connection = io('http://192.168.2.112:9000');

// connection is ready, now what? :) ->
connection.on( 'connect', () => {
  isConnectionActive = true;
} );

connection.on( 'disconnect', () => {
  isConnectionActive = false;
} );

// WebSocket event emitter function
let emitEvent = function( event ) {
  if( ! isConnectionActive ) {
    return alert( 'Server connection is closed!' );
  }

  // change button state
  if( event.target.id === 'button-turquoise') { button_turquoise_state = ! button_turquoise_state; }


  // emit `led-toggle` socket event
  connection.emit( 'led-toggle', {
    led: button_turquoise_state,
  } );



};
//what is e exactly, what does preventDefault do?
//https://socket.io/get-started/chat/
form.addEventListener('submit', (e)=> {
    e.preventDefault();
    if (input.value) {
      connection.emit('new input', input.value);
      input.value = '';
    }
  });


// add event listeners on button
button_turquoise.addEventListener( 'click', emitEvent );
