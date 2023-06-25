<template>
    <div class="dark:bg-gray-900">
        <div
            class="max-w-xl py-4 mx-auto text-center md:py-5 lg:py-10 lg:max-w-4xl"
        >
            <h2
                class="text-3xl font-semibold text-gray-800 capitalize lg:text-4xl xl:text-5xl dark:text-white pb-3"
                v-html="heading"
            ></h2>
            <p class="text-base text-gray-700 dark:text-slate-400 md:text-lg" v-html="description"></p>
        </div>
    </div>
</template>
<script>
export default {
    props: ["heading", "description"],
};
</script>
