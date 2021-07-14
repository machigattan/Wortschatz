const path = require( 'path' );
const express = require( 'express' );
const socketIO = require( 'socket.io' );
//const { spawn } = require ( 'child_process' );


//Import PythonShell module.
const { PythonShell } =require('python-shell');

// LED API wird importiert
const { toggle } = require( './led-control' );

// exrpess app wird erstellt
const app = express();

// yeet the index.html + http://<ip>:9000/ route - GET Methode 

app.get( '/', ( request, response ) => {
  response.sendFile( path.resolve( __dirname, 'web-application-wortschatz/index.html' ), {
    headers: {
      'Content-Type': 'text/html',
    }
  } );

} );

// bli bla blub, assets werden gesendet
app.use( '/assets/', express.static( path.resolve( __dirname, 'web-application-wortschatz' ) ) );
app.use( '/assets/', express.static( path.resolve( __dirname, 'node_modules/socket.io-client/dist' ) ) );

// server auf 9000 port
const server = app.listen( 9000, () => console.log( 'Express server started!' ) );

//  Websocket Server wird erstellt...
const io = socketIO( server );

// c o n n e c t   p l s
io.on( 'connection', ( client ) => {
  console.log( 'socket: ', 'someone connected', client.id );



//b y e b y e, wenn jemand disconnected
client.on( 'disconnect', () => {
console.log('A client disconnected')
});


    // Ist da ein toggle event?
    client.on( 'led-toggle', ( data ) => {
      console.log( 'an. aus. an. aus. :)' );
      toggle( data.led ); // toggle LEDs
    } );

//input Feld, listener für das event
client.on('new input', (msg)=> { 
     console.log('new word: ' + msg);

     //pass on arguments and execute script with python-shell
     let options = {
      mode: 'text',
      pythonPath: '/usr/bin/python3',
      pythonOptions: ['-u'], // get print results in real-time
      scriptPath: './',
      args: [msg]
  };
  
  PythonShell.run('writeRfid.py', options, function (err, results) {
      if (err) throw err;
      // results is an array consisting of messages collected during execution
      console.log('sending vocab (' + results + ') to python script');
  });
  });


} );