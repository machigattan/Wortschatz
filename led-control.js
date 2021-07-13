
// onoff importieren
const { Gpio } = require( 'onoff' );

// LED pin!
const pin_led = new Gpio( 26, 'out' );

// toggle that LED
exports.toggle = ( led ) => {
  pin_led.writeSync( led ? 1 : 0 );
};