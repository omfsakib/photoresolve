<script setup>
import ImageViewer from "../utility/ImageViewer.vue";
</script>
<template>
    <div class="dark:bg-gray-900">
        <div
            class="px-4 py-8 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8 lg:py-20"
        >
            <div class="grid gap-10 lg:grid-cols-2">
                <div class="flex items-center justify-center -mx-4 lg:pl-8">
                    <div class="px-3">
                        <ImageViewer
                            class="dark:opacity-70 object-cover w-40 h-40 rounded shadow-lg sm:h-64 xl:h-96 sm:w-64 xl:w-80 outline-0"
                            image="https://fixthephoto.com/images/uikit_slider/photo-manipulation-before1595251738_wh960.jpg"
                        />
                    </div>
                </div>

                <!-- left bar -->
                <div class="flex flex-col justify-center md:pr-8 xl:pr-0 lg:max-w-lg">
                    <div class="max-w-xl">
                        <h2
                            class="max-w-lg mb-6 font-sans text-3xl font-bold tracking-tight dark:text-white text-gray-900 sm:text-4xl sm:leading-none"
                        >
                            E-Commerce & Model Retouch
                        </h2>
                        <p class="text-base text-gray-700 dark:text-indigo-50 md:text-lg">
                            Specialized in professional E-Commerce & Fashion photo
                            retouching.
                        </p>
                        <div class="grid mt-2 lg:pt-3 lg:gap-10 lg:grid-cols-2">
                            <ul class="mb-3 lg:mb-4 -ml-1 space-y-2 dark:text-slate-300">
                                <li
                                    class="flex items-start"
                                    v-for="item in featureListLeft"
                                >
                                    <span class="mr-1">
                                        <svg
                                            class="w-5 h-5 mt-px text-blue-600"
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
                            <ul class="mb-3 lg:mb-4 -ml-1 space-y-2 dark:text-slate-300">
                                <li
                                    class="flex items-start"
                                    v-for="item in featureListRight"
                                >
                                    <span class="mr-1">
                                        <svg
                                            class="w-5 h-5 mt-px text-blue-600"
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
                    <div class="mb-5 font-normal text-base dark:text-slate-300">
                        Start From $0.90 - Photo
                    </div>
                    <div>
                        <router-link
                            :to="{ name: 'service-fashion' }"
                            aria-label=""
                            class="dark:text-slate-100 inline-flex items-center font-semibold text-xl transition-colors duration-200 text-blue-900 hover:text-deep-purple-800"
                        >
                            See more
                            <svg
                                class="inline-block w-3 ml-2"
                                fill="currentColor"
                                viewBox="0 0 12 12"
                            >
                                <path
                                    d="M9.707,5.293l-5-5A1,1,0,0,0,3.293,1.707L7.586,6,3.293,10.293a1,1,0,1,0,1.414,1.414l5-5A1,1,0,0,0,9.707,5.293Z"
                                ></path>
                            </svg>
                        </router-link>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data: () => ({
        featureListLeft: [
            "360° Degree",
            "Background Removal",
            "Ghost Mannequin",
            "Masking",
        ],
        featureListRight: [
            "Clean up & Retouching",
            "Shaping & Smoothies",
        ],
    }),
};
</script>
