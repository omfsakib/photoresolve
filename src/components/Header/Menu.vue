<template>
    <div class="hidden md:ml-10 md:block md:space-x-8 md:pr-4">
        <Popover class="relative inline-block" v-slot="{ open }">
            <PopoverButton
                class="group inline-block items-center text-[15px] font-Helvetica font-normal hover:text-slate-200 dark:text-slate-300 hover:dark:text-white outline-none"
                :class="[open ? 'text-slate-200' : 'text-white']"
            >
                <span>Services</span>
            </PopoverButton>

            <transition
                enter-active-class="transition ease-out duration-200"
                enter-from-class="opacity-0 translate-y-1"
                enter-to-class="opacity-100 translate-y-0"
                leave-active-class="transition ease-in duration-150"
                leave-from-class="opacity-100 translate-y-0"
                leave-to-class="opacity-0 translate-y-1"
            >
                <PopoverPanel
                    class="absolute z-10 -ml-4 mt-3 w-screen max-w-md transform px-2 sm:px-0 md:-translate-x-1/3 md:right-auto lg:left-1/4 lg:ml-0 lg:-translate-x-1/4"
                >
                    <div
                        class="overflow-hidden rounded-lg shadow-lg ring-1 ring-black ring-opacity-5"
                    >
                        <div
                            class="relative grid gap-6 bg-white dark:bg-gray-800 px-5 py-6 sm:gap-8 sm:p-8"
                        >
                            <router-link
                                active-class="active-mega-menu"
                                v-for="item in solutions"
                                :key="item.name"
                                :to="{ name: item.href }"
                                class="text-[15px] font-Helvetica font-normal -m-3 flex items-start rounded-lg p-3 hover:bg-gray-50 hover:dark:bg-gray-900"
                            >
                                <component
                                    :is="item.icon"
                                    class="h-6 w-6 flex-shrink-0 text-theme-color"
                                    aria-hidden="true"
                                />
                                <div class="ml-4 font-">
                                    <p
                                        class="text-sm font-Helvetica font-semibold text-gray-900 dark:text-white"
                                    >
                                        {{ item.name }}
                                    </p>
                                    <p
                                        class="mt-1 text-sm text-gray-500 dark:text-slate-400"
                                    >
                                        {{ item.description }}
                                    </p>
                                </div>
                            </router-link>
                        </div>
                    </div>
                </PopoverPanel>
            </transition>
        </Popover>

        <router-link
            class="text-[15px] font-Helvetica font-normal text-white hover:text-slate-200 dark:text-slate-300 hover:dark:text-white"
            v-for="item in navigation"
            :to="{ name: item.href }"
        >
            {{ item.name }}
        </router-link>
    </div>
</template>

<script setup>
import { Popover, PopoverButton, PopoverPanel } from "@headlessui/vue";
import {
    CursorArrowRaysIcon,
    ShieldCheckIcon,
    Squares2X2Icon,
    SparklesIcon,
    BuildingStorefrontIcon,
} from "@heroicons/vue/24/outline";

const solutions = [
    {
        name: "E-Commerce & Model Retouch",
        description: "",
        href: "service-fashion",
        icon: BuildingStorefrontIcon,
    },
    {
        name: "Product Retouching",
        description: "",
        href: "service-product",
        icon: Squares2X2Icon,
    },
    {
        name: "Jewelry Retouching",
        description: "",
        href: "service-jewelry",
        icon: SparklesIcon,
    },
    {
        name: "Other Services",
        description: "",
        href: "service-others",
        icon: ShieldCheckIcon,
    },
];
</script>

<script>
export default {
    data() {
    return {
      navigation: [],
    };
  },
  mounted() {
    fetch('https://app.photoresolve.com/getNavigation/')
      .then(response => response.json())
      .then(data => {
        this.navigation = data;
      })
      .catch(error => console.error(error));
  },
    computed: {
        currentRouteName() {
            return this.$route.name;
        },
    },
};
</script>
