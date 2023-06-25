<script setup>
import NewsLaterVue from "../components/pager/newslater.vue";
import axios from 'axios';
</script>
<template>
  <Header />

  <div class="dark:bg-gray-900">
    <div class="container mx-auto max-w-full md:max-w-full lg:max-w-screen-xl">
      <div class="flex flex-wrap -mx-4">
        <div class="w-full px-4">
          <div class="text-center mx-auto py-12 md:pr-11">
            <span class="font-semibold text-3xl text-theme-color dark:text-indigo-800 block">
              Portfolio
            </span>
            <h2 class="hidden font-bold text-3xl dark:text-white sm:text-4xl md:text-[40px] text-dark mb-4">
              Our Recent Works
            </h2>
            <p class="text-base text-body-color dark:text-slate-200"></p>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="dark:bg-gray-900">
    <lightgallery :settings="settings" class="mx-auto max-w-full md:max-w-full lg:max-w-screen-xl"
      id="animated-thumbnails-gallery">
      <a v-for="item in items" :key="item.id" className="gallery-item rounded-3xl cursor-pointer" :data-src="item.thumb">
        <img className="img-responsive rounded-3xl" :src="item.thumb" />
      </a>
    </lightgallery>
  </div>

  <Footer />
</template>

<script>
import Lightgallery from "lightgallery/vue";
import Header from "../components/Header/header.vue";

export default {
  components: {
    Lightgallery,
    Header,
  },
  data() {
    return {
      settings: {
        mode: 'lg-fade',
        mousewheel: 1,
        counter: 0,
        download: false,
        mobileSettings: {
          controls: false,
          download: false,
          counter: 0,
        },
      },
      items: [],
    };
  },
  mounted() {
    this.loadItems();
    this.$nextTick(() => {
      const myDiv = document.querySelector('.fullpage-wrapper');
      var body = document.body
      body.classList = 'fp-scroll-mac fp-viewing-0'
      if (myDiv) {
        myDiv.style.transform = 'translate3d(0px, 0px, 0px)';
        console.log(myDiv);
      }
    });
  },
  methods: {
    loadItems() {
      axios.get('https://app.photoresolve.com/getPortfolio/')
        .then((response) => {
          this.items = response.data.map((item) => ({
            id: item.id.toString(),
            src: item.src,
            thumb: item.thumb,
            size: item.size,
          }));
          this.initializeGallery();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    initializeGallery() {
      this.$nextTick(() => {
        jQuery('#animated-thumbnails-gallery').justifiedGallery({
          captions: true,
          lastRow: 'hide',
          rowHeight: 380,
          margins: 20,
        });
      });
    },
  },
};
</script>
