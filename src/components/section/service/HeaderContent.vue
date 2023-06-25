<script setup>
import FireIcon from "../../icon/fire.vue";
</script>
<template>
    <div
        class="relative mt-[-100px] pt-[130px] dark:bg-gray-900 min-h-[104vh] flex items-center justify-self-start  item-col ">
        <div class="ml-3 sm:ml-10 max-w-7xl">
            <div class="relative pb-8 sm:pb-16 md:pb-20 lg:w-full lg:max-w-2xl lg:pb-16">
                <main class="mt-10 max-w-7xl px-4 sm:mt-12 sm:px-6 md:mt-16 lg:mt-14 lg:px-8 xl:mt-18">
                    <div class="sm:text-center lg:text-left">
                        <h1 class="heading">
                            {{ title }}
                        </h1>
                        <p class="paragraph">
                            {{ content }}
                        </p>

                        <ul class="features-list mt-2 md:mt-4">
                            <li v-for="item in featureList" class="flex items-start font-medium text-black">
                                <span class="mr-1">
                                    <FireIcon class="w-5 h-5 mt-px text-theme-color" />
                                </span>
                                {{ item.name }}
                            </li>
                        </ul>
                    </div>
                </main>
            </div>
        </div>
        <div class="lg:absolute lg:z--10 lg:top-[100px] lg:right-0 lg:w-1/2" v-if="image">
            <img class="h-56 w-full object-contain sm:h-72 md:h-96 lg:h-full lg:w-full dark:brightness-50 image"
                :src="image" />
        </div>
    </div>
</template>

<script>
export default {
    props: ["title", "content", "image", "featureList"],
};
</script>
<style>
@media (min-width: 1024px) {
    .image {
        height: 500px;
    }
}

@media (max-width: 500px) {
    .item-col {
        display: flex;
        flex-direction: column-reverse;
        justify-content: flex-end;
    }
}
</style>
