import { createApp } from 'vue'

import router from "./router";
import App from './App.vue'

import page from '../public/page/page';
import Header from './components/Header/header.vue';
import Footer from './components/Footer/footer.vue';
import VueProgressBar from "@aacassandra/vue3-progressbar";

import 'vue-fullpage.js/dist/style.css'
import VueFullPage from 'vue-fullpage.js'


import './ImageComparisonSlide';
import './style.css'


const app = createApp(App);

/**
 *  Set default global properties
 */
app.config.globalProperties.$siteInfo = {
	"name": import.meta.env.VITE_APP_NAME,
	"siteURL": import.meta.env.VITE_APP_URL
};

app.config.globalProperties.$page = page;

app.use(router);
app.use(VueFullPage);
app.use(VueProgressBar, { color: '#4f46e5' });
app.component('Header', Header);
app.component('Footer', Footer);
app.mount("#app"); 
