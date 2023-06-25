<script setup>
import ImageViewer from "../utility/ImageViewer.vue";
</script>
<template>
    <div class="dark:bg-gray-900">
        <div
            class="px-4 py-16 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8 lg:py-20"
        >
            <div
                class="flex flex-col-reverse lg:grid max-w-screen-lg gap-8 lg:grid-cols-2 sm:mx-auto"
            >
                <div class="flex flex-col justify-center md:pr-8 xl:pr-0 lg:max-w-lg">
                    <div class="max-w-xl">
                        <h2
                            class="max-w-lg mb-6 font-sans text-3xl font-bold tracking-tight text-gray-900 dark:text-white sm:text-4xl sm:leading-none"
                        >
                            Product Retouching
                        </h2>
                        <p class="text-base dark:text-indigo-50 text-gray-700 md:text-lg">
                            We will help you to create more attractive image for your
                            product in order to stand out from the competition.
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
                        Start From $1.20 - Photo
                    </div>
                    <div>
                        <router-link
                            :to="{ name: 'service-product' }"
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

                <div class="grid grid-cols-2 gap-5">
                    <ImageViewer
                        class="dark:opacity-70 object-fill w-full h-72 col-span-2 rounded shadow-lg"
                        beforeImage="https://fixthephoto.com/images/uikit_slider/product-photo-editing-before1595333874_wh960.jpg"
                        afterImage="https://fixthephoto.com/images/uikit_slider/product-photo-editing-after1595333876_wh960.jpg"
                        fullscreen="true"
                    />

                    <ImageViewer
                        class="dark:opacity-70 object-fill w-full h-48 rounded shadow-lg"
                        beforeImage="/compare/product-retouching-bra-before.jpg"
                        afterImage="/compare/product-retouching-bra-after.jpg"
                        fullscreen="true"
                    />

                    <ImageViewer
                        class="dark:opacity-70 object-fill w-full h-48 rounded shadow-lg"
                        beforeImage="/compare/bag-before.jpg"
                        afterImage="/compare/bag-after.jpg"
                        fullscreen="true"
                    />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data: () => ({
        featureListLeft: [
            "Background Remove",
            "Product Cleaning",
            "Shadow Preserved",
            "Shadow Recreate",
        ],
        featureListRight: ["Clipping", "Color Change", "RAW Processing"],
    }),
};
</script>
