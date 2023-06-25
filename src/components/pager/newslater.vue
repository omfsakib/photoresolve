<template>
    <section class="bg-white w-full dark:bg-gray-900 px-6 mx-auto">
        <div
            class="container px-4 py-16 mx-auto lg:flex lg:items-center lg:justify-between sm:max-w-xl md:max-w-xl lg:max-w-screen-xl md:px-24 lg:px-8"
        >
            <h1
                class="text-xl font-normal font-Montserrat text-gray-800 md:text-xl xl:text-2xl dark:text-white"
            >
                Do you need professional photo editing?
                <span
                    class="text-theme-color mt-3 font-Montserrat font-medium text-2xl xl:text-3xl block"
                >
                    Send us an email.
                </span>
            </h1>

            <div class="mt-8">
                <div class="flex flex-col space-y-3 sm:space-y-0 sm:flex-row sm:-mx-2">
                    <input
                        v-show="false"
                        id="email"
                        type="text"
                        class="px-4 py-2 text-gray-700 bg-white border border-gray-300 rounded-md sm:mx-2 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-600 outline-none"
                        placeholder="Email Address"
                    />

                    <router-link
                        :to="{ name: 'contact' }"
                        class="text-center sm:text-left px-6 sm:px-12 py-3 text-sm font-medium tracking-wide text-white capitalize transition-colors duration-300 transform bg-theme-color hover:bg-slate-900 hover:dark:bg-zinc-800 dark:bg-gray-800 dark:text-slate-200 rounded-md sm:mx-2 outline-none"
                    >
                        Get Started
                    </router-link>
                </div>
            </div>
        </div>
    </section>
</template>
