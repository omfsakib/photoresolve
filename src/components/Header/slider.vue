<script setup>
import ActionForm from "./action.form.vue";
</script>
<template>
    <section
        class="bg-slate-50 dark:bg-gray-900 flex items-center justify-between px-4 sm:px-6 lg:px-8 py-4 mx-auto slider-h"
    >
        <main
            class="mx-auto max-w-7xl px-4 sm:mt-12 sm:px-6 md:mt-16 lg:mt-14 lg:px-8 xl:mt-18"
        >
            <div class="sm:text-center lg:text-left">
                <h1 class="font-Helvetica font-normal tracking-tight text-gray-900 dark:text-white">
                    <div class="text-2xl md:text-3xl lg:text-[35px]" id="master-container-scroller">
                      <div v-for="item in items" :class="[item.class, 'master-container-scroller_item']">
                        {{ item.text }}
                      </div>
                    </div>
                </h1>
                <p
                    class="mt-3 text-sm sm:text-lg font-Montserrat font-normal text-black dark:text-slate-200 sm:mx-auto sm:mt-5 sm:max-w-xl lg:mx-0"
                    v-html="slide.caption"
                ></p>

            </div>
        </main>
        <div class="hidden md:block md:inset-y-0 md:right-0 md:w-1/2">
            <img
                v-if="slide.cover"
                class="h-56 w-full object-contain sm:h-72 md:h-96 lg:h-full lg:w-full dark:brightness-50"
                :src="slide.cover"
            />
        </div>
    </section>
</template>

<script>
export default {
    data() {
    return {
      items: [],
      slide: {},
    };
  },
  mounted() {
    this.fetchSlideText();
  },
  methods: {
    async fetchSlideText() {
      try {
        const response = await fetch('https://app.photoresolve.com/getSlideText/');
        this.items = await response.json();

        const infoResponse = await fetch('https://app.photoresolve.com/getSlideInfo/');
        this.slide = await infoResponse.json();

      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>
