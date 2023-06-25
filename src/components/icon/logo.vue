<template>
    <svg v-if="logo" v-html="logo" class="w-8" viewBox="0 0 24 24" stroke-linejoin="round" stroke-width="2" stroke-linecap="round" stroke-miterlimit="10" stroke="#ffffff" fill="none" aria-label="logo" title="Home Page"></svg>
</template>
<script>
export default {
  data() {
    return {
      logo: null,
    };
  },
  mounted() {
    fetch('https://app.photoresolve.com/getLogo/')
      .then(response => response.text())
      .then(svgCode => {
        this.logo = svgCode;
      });
  },
};
</script>