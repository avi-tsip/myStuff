const EventEmitter = require("events");

const customEmitter = new EventEmitter()

customEmitter.on('response', (name, id)=>{
    console.log(`data received from ${name} with and id of ${id}`)
})
customEmitter.on('response', ()=>{
    console.log('listen to another event ')
})

customEmitter.emit('response', 'jhon', 51)
