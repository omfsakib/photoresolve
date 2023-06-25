<template>
    <transition
        enter-active-class="duration-150 ease-out"
        enter-from-class="opacity-0 scale-95"
        enter-to-class="opacity-100 scale-100"
        leave-active-class="duration-100 ease-in"
        leave-from-class="opacity-100 scale-100"
        leave-to-class="opacity-0 scale-95"
    >
        <PopoverPanel
            focus
            class="absolute inset-x-0 top-0 z-10 origin-top-right transform p-2 transition md:hidden"
        >
            <div
                class="overflow-hidden relative rounded-lg bg-white dark:bg-gray-900 h-[97vh] shadow-md ring-1 ring-black ring-opacity-5"
            >
                <div class="flex items-center justify-between px-5 pt-4">
                    <div></div>
                    <div class="-mr-2">
                        <PopoverButton
                            class="inline-flex items-center justify-center rounded-md bg-white dark:bg-gray-700 hover:dark:bg-gray-700 p-2 text-gray-400 hover:bg-gray-100 hover:text-gray-500 hover:dark:text-stone-200 outline-none"
                        >
                            <span class="sr-only">Close main menu</span>
                            <XMarkIcon class="h-6 w-6" aria-hidden="true" />
                        </PopoverButton>
                    </div>
                </div>
                <div class="space-y-1 px-2 pt-2 pb-3">
                    <router-link
                        v-for="item in navigation"
                        :key="item.name"
                        :to="{ name: item.href }"
                        class="block rounded-md px-3 py-2 text-base font-medium text-gray-700 hover:bg-gray-50 hover:text-gray-900 dark:text-slate-300 hover:dark:text-white hover:dark:bg-gray-700"
                        >{{ item.name }}
                    </router-link>
                </div>
                <router-link
                    :to="{ name: 'contact' }"
                    class="absolute bottom-0 block w-full bg-gray-50 dark:bg-gray-700 dark:text-slate-300 px-5 py-3 text-center font-medium text-indigo-600 hover:bg-gray-100"
                >
                    start now
                </router-link>
            </div>
        </PopoverPanel>
    </transition>
</template>

<script setup>
import { XMarkIcon } from "@heroicons/vue/24/outline";
import { PopoverButton, PopoverPanel } from "@headlessui/vue";
const navigation = [
    { name: "E-Commerce & Model Retouch", href: "service-fashion" },
    { name: "Product Retouching", href: "service-product" },
    { name: "Jewelry Retouching", href: "service-jewelry" },
    { name: "Other Services", href: "service-others" },
    { name: "Portfolio", href: "portfolio" },
    { name: "Pricing", href: "prices" },
    { name: "Contact", href: "contact" },
];
</script>
