<script setup>
import NewsLaterVue from "../components/pager/newslater.vue";

</script>
<template>
    <full-page ref="fullpage" :options="options">
        <div class="section" id="section" style="justify-content: flex-start;">
            <Header />

            <section class="bg-white dark:bg-gray-900 full-page-flex !items-start">
                <div class="container px-6 mx-auto">
                    <div class="lg:flex lg:items-baseline lg:-mx-6">
                        <div class="lg:w-1/2 lg:mx-6">
                            <h1 class="text-2xl lg:text-3xl font-Helvetica font-normal text-black dark:text-white">
                                Ultimate image post production solutions
                                <div class="text-xl md:text-3xl text-theme-color font-Montserrat font-normal mt-1.5"></div>
                            </h1>

                            <p class="max-w-xl mt-6 text-sm dark:text-slate-50" v-html="contact.caption"></p>

                            <div class="mt-6 space-y-7 md:mt-8">
                                <p class="flex items-start -mx-2" v-if="contact.phone">
                                    <svg xmlns="http://www.w3.org/2000/svg"
                                        class="w-6 h-6 mx-2 text-theme-color dark:text-blue-400" fill="none"
                                        viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                                        <path stroke-linecap="round" stroke-linejoin="round"
                                            d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                                    </svg>

                                    <span class="mx-2 text-black truncate w-72 dark:text-gray-400"
                                        v-html="contact.phone"></span>
                                </p>

                                <a v-if="contact.email" :href="'mailto:' + contact.email"
                                    class="inline-flex items-start -mx-2">
                                    <svg xmlns="http://www.w3.org/2000/svg"
                                        class="w-6 h-6 mx-2 text-theme-color dark:text-blue-400" fill="none"
                                        viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                                        <path stroke-linecap="round" stroke-linejoin="round"
                                            d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                                    </svg>

                                    <span class="w-fit mx-2 text-black truncate dark:text-gray-400"
                                        v-html="contact.email"></span>
                                </a>

                                <p v-if="contact.address" class="flex items-start -mx-2">
                                    <svg xmlns="http://www.w3.org/2000/svg"
                                        class="w-6 h-6 mx-2 text-theme-color dark:text-blue-400" fill="none"
                                        viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                                        <path stroke-linecap="round" stroke-linejoin="round"
                                            d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                                        <path stroke-linecap="round" stroke-linejoin="round"
                                            d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                                    </svg>

                                    <span class="mx-2 text-black truncate w-72 dark:text-gray-400" v-html="contact.address">
                                    </span>
                                </p>
                            </div>
                        </div>

                        <div class="mt-8 lg:w-1/2 lg:mx-6">
                            <div
                                class="w-full px-8 py-10 mx-auto overflow-hidden bg-white rounded-lg shadow-2xl dark:bg-gray-900 lg:max-w-xl shadow-gray-300/50 dark:shadow-black/50">
                                <h1 class="text-lg font-medium text-black dark:text-slate-50">
                                    Send us your queries
                                </h1>

                                <form method="POST" @submit.prevent="submitForm" class="mt-6">
                                    <div class="flex-1">
                                        <label class="block mb-2 text-sm text-black dark:text-gray-200">Full Name</label>
                                        <input type="text" name="name" placeholder="John Doe"
                                            class="block w-full px-3 py-2 mt-2 text-black placeholder-gray-400 bg-white border border-gray-200 rounded-md dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40" />
                                    </div>

                                    <div class="flex-1 mt-6">
                                        <label class="block mb-2 text-sm text-black dark:text-gray-200">Email
                                            address</label>
                                        <input type="email" name="email" placeholder="johndoe@example.com"
                                            class="block w-full px-3 py-2 mt-2 text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-md dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40" />
                                    </div>

                                    <div class="w-full mt-6">
                                        <label class="block mb-2 text-sm text-black dark:text-gray-200">Message</label>
                                        <textarea
                                            class="block w-full h-20 px-3 py-2 mt-2 text-black placeholder-gray-400 bg-white border border-gray-200 rounded-md dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40"
                                            placeholder="Message" name="message"></textarea>
                                    </div>

                                    <button type="submit"
                                        class="w-full px-6 py-3 mt-6 text-sm font-medium tracking-wide text-white capitalize transition-colors duration-300 transform bg-theme-color rounded-md hover:bg-slate-900 hover:dark:bg-zinc-800 dark:bg-gray-800 dark:text-slate-200">
                                        get in touch
                                    </button>
                                </form>

                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </div>

        <Footer />
    </full-page>
</template>
<style>
.full-page-flex{
    min-height: 87vh !important;
}
</style>
<script>
import axios from "axios";

export default {
    data() {
        return {
            contact: {},
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
        axios.get("https://app.photoresolve.com/getContact/")
            .then(response => {
                this.contact = response.data;
            })
            .catch(error => console.log(error));



        this.$refs.fullpage.api.silentMoveTo('first', 1);
    },
    methods: {
        async submitForm() {
            const form = new FormData(event.target);
            try {
                const response = await axios.post('https://app.photoresolve.com/postQuery/', form);
                console.log(response.data);
                // Redirect to home page
                window.location.href = '/';

                // Clear the form fields
                event.target.reset();

            } catch (error) {
                console.log(error);
            }
        },

    }
};
</script>
