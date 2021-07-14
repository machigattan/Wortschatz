const { expect } = require('chai');
const io = require('socket.io-client');
  
const socketURL = `http://${process.env.IP}:${process.env.PORT}`;
  
  describe('connect (Team 5 who)', () => {
    it('emit emit emit emit emit', (done) => {
      const socket = io(`${socketURL}?browserId=someBrowserId`);
      socket.on('connected', (data) => {
        expect(data.message).to.equal('connected');
        socket.disconnect();
        done();
      });
    });
  });