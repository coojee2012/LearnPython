<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png" v-bind:title="message">
    <a-button type="primary" v-on:click="reverseMessage" >{{message}}</a-button>
    <a-button type="info" v-stream:click="plus$" >+</a-button>
    <ol>
      <li v-for="todo in todos" v-bind:key='todo.id'>
        {{ todo.text }}
        {{msg2}}
      </li>
    </ol>
    <span>{{ count }}</span>
    <input v-model="message">
    <HelloWorld msg="Welcome to Your Vue.js App"/> 
  </div>
</template>

<script>
import { Observable,interval,Subject } from 'rxjs';
import { map,startWith,scan } from 'rxjs/operators';

import HelloWorld from './components/HelloWorld.vue'


export default {
  name: 'app',
  subscriptions() {
    // 声明接收的 Subjects
    this.plus$ = new Subject();

    return {
      msg: new Observable(observer => {
            let number = 1
              setInterval(() => {
                observer.next(number++)
              }, 1000)
          }),
      msg2: interval(1000).pipe(map(x => x * x)),
      count: this.plus$.pipe(
        map(() => 1),
        startWith(0),
        scan((total, change) => total + change)
      )
    };
  },
  data() {
    return {
      'message': 'Hello Btn',
      todos:[ {
        id:1,
        text:"ddd1"
      },
       {
        id:2,
        text:"ddd2"
      },
       {
        id:3,
        text:"ddd3"
      }],
      };
  },
  methods:{
    reverseMessage:function() {
      this.message = this.message.split('').reverse().join('')
    }
  },
  components: {
    HelloWorld
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
