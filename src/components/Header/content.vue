<template>
    <main
        class="mx-auto max-w-7xl px-4 sm:mt-12 sm:px-6 md:mt-16 lg:mt-14 lg:px-8 xl:mt-18"
    >
        <div class="sm:text-center lg:text-left">
            <h1 class="font-bold tracking-tight text-gray-900 dark:text-white">
                <div
                    class="text-3xl md:text-5xl lg:text-[50px]"
                    id="master-container-scroller"
                >
                    <div class="text-indigo-600 master-container-scroller_item">
                        E-commerce
                    </div>
                    <div class="text-red-600 master-container-scroller_item">
                        Fashion & Model
                    </div>
                    <div class="text-indigo-900 master-container-scroller_item">
                        Jewelry Retouching
                    </div>
                    <div class="text-fuchsia-700 master-container-scroller_item">
                        Potrait & Headshot
                    </div>
                    <div class="text-pink-600 master-container-scroller_item">
                        Wedding Images
                    </div>
                    <div class="text-rose-900 master-container-scroller_item">
                        Color Correction
                    </div>
                    <div class="text-yellow-500 master-container-scroller_item">
                        360° Image Editing
                    </div>
                    <div class="text-orange-600 master-container-scroller_item">
                        Background Removal
                    </div>
                    <div class="text-slate-600 master-container-scroller_item">
                        Clean up & Retouching
                    </div>
                    <div class="text-indigo-600 master-container-scroller_item">
                        Ghost Mannequin
                    </div>
                    <div class="text-indigo-900 master-container-scroller_item">
                        Skin Retouch
                    </div>
                    <div class="text-indigo-900 master-container-scroller_item">
                        Wrinkles Removal
                    </div>
                </div>
            </h1>
            <p
                class="mt-3 text-base text-gray-500 dark:text-slate-200 sm:mx-auto sm:mt-5 sm:max-w-xl sm:text-lg md:mt-5 md:text-xl lg:mx-0"
            >
                Sleek your images with our Professional & Creative Image editing agency
            </p>

            <ActionForm />
        </div>
    </main>
</template>

<script setup>
import ActionForm from "./action.form.vue";
</script>
