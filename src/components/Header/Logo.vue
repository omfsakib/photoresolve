<template>
    <router-link
        :to="{ name: 'home' }"
        class="flex flex-shrink-0 flex-grow items-center lg:flex-grow-0 cursor-pointer"
    >
        <div class="flex w-full items-center justify-between md:w-auto">
            <Logo />
            <span class="text-white ml-2 text-xl font-normal tracking-wide uppercase">
                photo resolve
            </span>

            <div class="-mr-2 flex items-center md:hidden">
                <PopoverButton
                    class="inline-flex items-center justify-center rounded-md bg-white p-2 text-gray-400 hover:bg-gray-100 hover:text-gray-500 dark:bg-gray-800 outline-none"
                >
                    <span class="sr-only">Open main menu</span>
                    <Bars3Icon class="h-6 w-6" aria-hidden="true" />
                </PopoverButton>
            </div>
        </div>
    </router-link>
</template>

<script setup>
import { PopoverButton } from "@headlessui/vue";
import { Bars3Icon } from "@heroicons/vue/24/outline";
import Logo from "@/components/icon/logo.vue";
</script>
