
<template>
  <Header />
  <div class="bg-white dark:bg-gray-900">
    <section class="container mx-auto max-w-full md:max-w-full lg:max-w-screen-xl">
      <div class="px-4 md:px-8 lg:px-16 py-6 md:py-12" v-html="myHtml">
      </div>
    </section>
  </div>
  <HowITWorkVue />
  <Footer />
</template>



<script>
import HowITWorkVue from '.././components/pager/how-it-work.vue'
import axios from 'axios';
export default {
  data() {
    return {
      myHtml: ''
    }
  },
  methods: {
    fetchPosts() {
      axios.get('https://app.photoresolve.com/getTermsAndConditions/')
        .then(response => {
          this.myHtml = response.data;
          console.log(response.data)
        })
        .catch(error => {
          console.error(error);
        });
    }
  },
  mounted() {
    this.fetchPosts();
  }
}
</script>






