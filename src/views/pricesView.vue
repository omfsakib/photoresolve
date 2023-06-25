<script setup>
import IconsRoundShape from "../components/icon/round-shape.vue";
import IconsRoundShapeCross from "../components/icon/round-shape-cross.vue";
</script>
<template>
    <full-page ref="fullpage" :options="options">
        <div class="section" style="justify-content: flex-start;">
            <Header />
            <div class="bg-white dark:bg-gray-900">
                <div class="container px-6 py-8 mx-auto lg:mt-10">
                    <h1 class="text-3xl lg:text-4xl font-black text-center text-gray-800 capitalize dark:text-white">
                        Pricing
                    </h1>

                    <!-- package items -->
                    <div class="grid grid-cols-1 gap-8 mt-6 lg:grid-cols-3 xl:mt-12">
                        <div class="package-holder" v-for="(data, key) in package"
                            :class="data.recommend ? '!border-theme-color' : ''" @click="setPackage(key)" :key="key">
                            <div class="package-body">
                                <IconsRoundShape :class="
                                    data.recommend
                                        ? '!text-theme-color !dark:text-blue-500'
                                        : ''
                                " class="w-5 h-5 text-gray-400 sm:h-7 sm:w-7" />
                                <h2 class="package-title" v-html="data.name"></h2>
                            </div>

                            <div class="flex flex-col items-center space-y-1" v-if="data.price">
                                <div class="package-price-discount" v-if="data.price.discount" v-html="data.price.discount">
                                </div>

                                <h2 class="package-price-tag" :class="
                                    data.recommend
                                        ? '!text-theme-color !dark:text-blue-500'
                                        : ''
                                ">
                                    <div class="text-xs text-indigo-500" v-if="data.price.start" v-html="data.price.start">
                                    </div>

                                    <span v-html="data.price.value"></span>
                                    <span class="text-base font-medium pl-2" v-if="data.price.duration"
                                        v-html="data.price.duration"></span>
                                </h2>
                            </div>
                        </div>
                    </div>

                    <!-- package body -->
                    <div class="package-item-body" v-if="0">
                        <div class="flex items-center justify-between text-black dark:text-gray-200"
                            v-for="item in packageIteam">
                            <p class="text-base font-Helvetica font-thin" v-text="item.name"></p>
                            <IconsRoundShape class="w-5 h-5 text-blue-500 sm:h-7 sm:w-7" v-if="item.access" />
                            <IconsRoundShapeCross class="w-5 h-5 text-red-400 sm:h-7 sm:w-7" v-else />
                        </div>
                    </div>

                    <div class="flex justify-center mt-8">
                        <button @click="$router.push({ name: 'contact' })"
                            class="px-8 py-2 tracking-wide text-white capitalize transition-colors duration-300 transform bg-theme-color rounded-md hover:bg-slate-900 focus:outline-none hover:dark:bg-zinc-800 dark:bg-gray-800 dark:text-slate-200">
                            start now
                        </button>
                    </div>
                </div>
            </div>

            <div class="text-center pt-14 pb-6 md:py-10 dark:bg-gray-900">
                <h1 @click="$router.push({ name: 'contact' })"
                    class="text-xl font-medium text-gray-800 lg:text-2xl xl:text-4xl dark:text-white">
                    Looking for something else?<br />
                    <div
                        class="text-theme-color hover:text-slate-900 capitalize mt-4 font-semibold cursor-pointer text-xl xl:text-4xl inline-block">
                        contact us
                    </div>
                </h1>
            </div>
        </div>
        <Footer />
    </full-page>
</template>

<script>
import NewsLaterVue from "../components/pager/newslater.vue";
import axios from "axios";
export default {
    components: {
        NewsLaterVue,
    },
    data() {
        return {
            package: {},
            options: {
                licenseKey: "gplv3-license",
                responsiveWidth: 800,
                navigation: false,
                anchors: ['first', 'second', 'third'],

                // other options
            },
        };
    },

    mounted() {
        axios.get("https://app.photoresolve.com/getPricing/")
            .then(response => {
                this.package = response.data.reduce((acc, item) => {
                    acc[item.name] = {
                        name: item.name,
                        price: {
                            value: `$ ${item.price.toFixed(2)}`,
                            start: "starts from",
                            discount: "",
                            duration: "/ Per Photo",
                        },
                        recommend: 0,
                    };
                    return acc;
                }, {});
            })
            .catch(error => console.log(error));
        this.$refs.fullpage.api.silentMoveTo('first', 1);
    },
};
</script>
