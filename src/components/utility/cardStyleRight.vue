<script setup>
import ImageViewer from "../utility/ImageViewer.vue";
</script>
<template>
    <div class="dark:bg-gray-900 full-page-flex">
        <div
            class="px-4 mb-8 sm:mb-0 sm:py-16 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8 lg:py-20"
        >
            <div
                class="flex flex-col-reverse sm:grid pt-10 sm:pt-0 gap-10 lg:grid-cols-2"
            >
                <div
                    class="flex flex-col justify-center md:pr-8 xl:pr-0 lg:max-w-lg sm:pl-3"
                >
                    <div class="max-w-xl">
                        <router-link
                            class="heading"
                            :class="
                                card.page ? 'cursor-pointer hover:text-indigo-900' : ''
                            "
                            :to="{ name: card.page }"
                        >
                            {{ card.title }}
                        </router-link>
                        <p class="paragraph">
                            {{ card.content }}
                        </p>
                        <div
                            class="grid mt-2 lg:pt-3 lg:gap-10 lg:grid-cols-2"
                            v-if="
                                card.featureList ||
                                card.featureList.Left ||
                                card.featureList.Right
                            "
                        >
                            <ul class="features-list">
                                <li
                                    class="flex items-start"
                                    v-for="item in card.featureList.Left"
                                >
                                    <span class="mr-1">
                                        <svg
                                            class="w-5 h-5 mt-px text-theme-color"
                                            stroke="currentColor"
                                            viewBox="0 0 52 52"
                                        >
                                            <polygon
                                                stroke-width="4"
                                                stroke-linecap="round"
                                                stroke-linejoin="round"
                                                fill="none"
                                                points="29 13 14 29 25 29 23 39 38 23 27 23"
                                            ></polygon>
                                        </svg>
                                    </span>
                                    {{ item }}
                                </li>
                            </ul>
                            <ul class="features-list">
                                <li
                                    class="flex items-start"
                                    v-for="item in card.featureList.Right"
                                >
                                    <span class="mr-1">
                                        <svg
                                            class="w-5 h-5 mt-px text-theme-color"
                                            stroke="currentColor"
                                            viewBox="0 0 52 52"
                                        >
                                            <polygon
                                                stroke-width="4"
                                                stroke-linecap="round"
                                                stroke-linejoin="round"
                                                fill="none"
                                                points="29 13 14 29 25 29 23 39 38 23 27 23"
                                            ></polygon>
                                        </svg>
                                    </span>
                                    {{ item }}
                                </li>
                            </ul>
                        </div>
                    </div>
                    <div class="mb-1 sm:my-3 font-normal dark:text-slate-200 text-sm">
                        {{ card.start }}
                    </div>
                    <div class="mt-3">
                        <router-link
                            :to="{ name: card.link }"
                            class="text-sm px-6 py-2 sm:py-3 font-medium tracking-wide text-white capitalize transition-colors duration-300 transform bg-theme-color hover:bg-slate-900 rounded-md"
                        >
                            Get a free quote
                            <svg
                                class="inline-block w-3 ml-1 text-white"
                                fill="#fff"
                                viewBox="0 0 12 12"
                            >
                                <path
                                    d="M9.707,5.293l-5-5A1,1,0,0,0,3.293,1.707L7.586,6,3.293,10.293a1,1,0,1,0,1.414,1.414l5-5A1,1,0,0,0,9.707,5.293Z"
                                ></path>
                            </svg>
                        </router-link>
                    </div>
                </div>
                <div class="flex items-center justify-center -mx-4 lg:pl-8">
                    <div class="px-3">
                      <img :src="card.cover.image" class="object-cover rounded w-60 h-60 sm:w-64 sm:h-64 xl:w-80 xl:h-80">
                    </div>
                  </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    props: ["card"],
};
</script>