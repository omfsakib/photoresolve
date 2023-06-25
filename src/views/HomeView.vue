<script setup>
import Slider from "../components/Header/slider.vue";
import OrtherServiceVue from "../components/section/orther.service.vue";
import HowITWorkVue from "../components/pager/how-it-work.vue";
import left from "@/components/utility/cardStyleLeft.vue";
import right from "@/components/utility/cardStyleRight.vue";

import axios from 'axios';
</script>
<template>
  <full-page ref="fullpage" :options="options" id="fullpage">
    <div class="section">
      <Header />
      <Slider :slide="slide" />
    </div>
    <component v-for="(item, index) in card" :key="index" :is="item.viewType == 'left' ? left : right" :card="item"
      class="section" />

    <HowITWorkVue />
    <Footer />
  </full-page>
</template>

<script>
export default {
  data() {
    return {
      options: {
        licenseKey: "gplv3-license",
        responsiveWidth: 800,
        navigation: false,
        anchors: ['first', 'second', 'third'],

        // other options
      },
      slide: this.$page.home.slide,
      card: {
        item1: {
          title: "",
          button_name: "",
          content: "",
          start: "",
          page: "service-fashion",
          link: "contact",
          cover: {
            image: "",
            before: "",
          },
          featureList: {
            Left: [

            ],
            Right: [

            ],
          },
          viewType: 'left',
        },
        item2: {
          title: "",
          button_name: "",
          content: "",
          start: "",
          page: "service-product",
          link: "contact",
          cover: {
            image: "",
            before: "",
          },
          featureList: {
            Left: [

            ],
            Right: [

            ],
          },
          viewType: 'right',
        },
        item3: {
          title: "",
          button_name: "",
          page: "service-jewelry",
          content: "",
          start: "",
          link: "contact",
          cover: {
            image: "",
            before: "",
          },
          featureList: {
            Left: [

            ],
            Right: [

            ],
          },
          viewType: 'left',
        },
        item4: {
          title: "",
          button_name: "",
          page: "service-others",
          content: "",
          start: "",
          link: "contact",
          cover: {
            image: "",
            before: "",
          },
          featureList: {
            Left: [

            ],
            Right: [

            ],
          },
          viewType: 'right',
        },
      },
    };
  },
  methods: {
    fetchPosts() {
      axios.get('https://app.photoresolve.com/getServices/')
        .then(response => {
          const data = response.data;
          this.card.item1.title = data.item1.title;
          this.card.item1.button_name = data.item1.button_name;
          this.card.item1.content = data.item1.content;
          this.card.item1.start = data.item1.start;
          this.card.item1.cover.image = data.item1.cover.image;
          this.card.item1.featureList.Left = data.item1.featureList.Left;
          this.card.item1.featureList.Right = data.item1.featureList.Right;

          this.card.item2.title = data.item2.title;
          this.card.item2.button_name = data.item2.button_name;
          this.card.item2.content = data.item2.content;
          this.card.item2.start = data.item2.start;
          this.card.item2.cover.image = data.item2.cover.image;
          this.card.item2.featureList.Left = data.item2.featureList.Left;
          this.card.item2.featureList.Right = data.item2.featureList.Right;

          this.card.item3.title = data.item3.title;
          this.card.item3.button_name = data.item3.button_name;
          this.card.item3.content = data.item3.content;
          this.card.item3.start = data.item3.start;
          this.card.item3.cover.image = data.item3.cover.image;
          this.card.item3.featureList.Left = data.item3.featureList.Left;
          this.card.item3.featureList.Right = data.item3.featureList.Right;

          this.card.item4.title = data.item4.title;
          this.card.item4.button_name = data.item4.button_name;
          this.card.item4.content = data.item4.content;
          this.card.item4.start = data.item4.start;
          this.card.item4.cover.image = data.item4.cover.image;
          this.card.item4.featureList.Left = data.item4.featureList.Left;
          this.card.item4.featureList.Right = data.item4.featureList.Right;
        })
        .catch(error => {
          console.error(error);
        });
    }
  },
  mounted() {
    this.fetchPosts();
    this.$refs.fullpage.api.silentMoveTo('first', 1);
  }
};
</script>
<style></style>
