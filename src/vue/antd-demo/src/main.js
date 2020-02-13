import Vue from 'vue'
import VueRx from 'vue-rx';
import { Button } from 'ant-design-vue';
import App from './App.vue'

Vue.use(VueRx);

Vue.component(Button.name, Button);
Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
