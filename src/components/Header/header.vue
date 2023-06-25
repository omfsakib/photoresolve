<script setup>
import { Popover } from "@headlessui/vue";
import HeaderLogo from "./Logo.vue";
import HeaderMenu from "./Menu.vue";
import MobileMenu from "./mobile.menu.vue";
</script>
<template>
    <header
        class="relative z-10 bg-theme-color text-white dark:bg-gray-900 dark:border-b dark:border-slate-50"
    >
        <div class="mx-auto max-w-7xl">
            <div class="relative w-full">
                <Popover>
                    <div class="relative px-4 sm:px-6 lg:px-8 py-4">
                        <nav class="relative flex items-center justify-between sm:h-10" style="margin-top: 1px;">
                            <HeaderLogo />
                            <HeaderMenu />
                        </nav>
                    </div>
                    <MobileMenu />
                </Popover>
            </div>
        </div>
    </header>
</template>
