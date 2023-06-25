<template>
    <div class="action-form">
        <div class="mt-4 md:col-span-2 md:mt-14">
            <div
                class="text-base sm:text-lg text-black dark:text-indigo-100 mt-4 font-medium"
            >
                Do you need professional photo editing?
            </div>

            <form v-on:submit.prevent>
                <div class="overflow-hidden">
                    <div class="px-0 py-1">
                        <div
                            class="flex items-end justify-start mt-1 sm:justify-center sm:items-stretch gap-1 grid-cols-2 md:mt-5 md:flex md:justify-center lg:grid lg:gap-6 lg:mt-0"
                        >
                            <div class="text-left w-full sm:w-auto">
                                <label
                                    for="company-website"
                                    class="block text-sm font-medium dark:text-indigo-100 text-gray-900"
                                >
                                    Contact us to resolve your need.
                                </label>
                                <div class="mt-1 flex-shrink-0">
                                    <input
                                        type="text"
                                        name="company-website"
                                        id="company-website"
                                        class="relative text-sm inline w-full appearance-none rounded border shadow-sm px-3 py-2 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-600 border-gray-300 text-gray-900 placeholder-gray-500 focus:border-indigo-500 focus:ring-indigo-500 focus:outline-none focus:z-10"
                                        placeholder="Enter Your Email"
                                    />
                                </div>
                            </div>

                            <div class="text-left sm:py-6 min-w-[90px]">
                                <button
                                    type="submit"
                                    class="inline-flex justify-center rounded-md border border-transparent py-2 px-4 text-sm font-medium text-white shadow-sm outline-none bg-theme-color hover:bg-slate-900 hover:dark:bg-zinc-800 dark:bg-gray-800 dark:text-slate-200"
                                >
                                    Email Us
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>
