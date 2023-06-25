
<template>
    <!-- single image show without compare image -->
    <img :src="image" :class="class" v-if="!compare" @click="fullscreenImage" />

<!-- compare show -->
<img-comparison-slider
    @click="fullscreenImage"
    class="cursor-pointer outline-0"
    :class="class"
    v-else
>
    <img slot="first" :class="class" :src="beforeImage" />
    <img slot="second" :class="class" :src="afterImage" />
</img-comparison-slider>

<div
    v-show="isModalVisible"
    v-if="fullscreen"
    class="bg-slate-900/80 overflow-hidden fixed top-0 right-0 left-0 z-50 w-full h-full"
>
    <div class="relative w-full h-full m-auto">
        <!-- Modal content -->
        <div class="relative h-full text-center mr-auto">
            <button
                type="button"
                @click="close"
                class="fixed top-1 right-2.5 z-10 md:z-auto bg-slate-100 text-cyan-900 rounded-md text-sm md:text-lg leading-tight py-1 px-1 md:px-2.5 dark:bg-cyan-900 dark:text-white"
                data-modal-toggle="extralarge-modal"
            >
                close
                <div class="backdrop" @click="close"></div>
            </button>
            <!-- Modal body -->
            <div class="!h-full flex justify-center items-center">
                <!-- single image show without compare image -->
                <img
                    :src="image"
                    class="w-auto h-full max-w-full max-h-full text-center m-auto object-cover outline-0"
                    v-if="!compare"
                    @click.stop
                />

                <!-- compare show -->
                <img-comparison-slider
                    @click="fullscreenImage"
                    class="object-cover converResponsive outline-0"
                    v-else
                >
                    <img slot="first" :src="beforeImage" />
                    <img slot="second" :src="afterImage" />
                </img-comparison-slider>
            </div>
        </div>
    </div>
</div>

</template>
<style>
.converResponsive {
    width: auto;
    height: 100%;
    max-width: 100%;
    max-height: 100%;
}
@media (max-width: 640px) {
    .converResponsive {
        width: 100%;
        height: auto;
    }
    .backdrop {
        position: unset !important;
    }
}

.converResponsive img {
    width: auto;
    height: 100%;
    max-width: 100%;
    max-height: 100%;
    object-fit: fill;
    user-select: none;
}

.backdrop {
    position: fixed;
    top: 0;
    left: 0;
    width: 100% !important;
    height: 100% !important;
    cursor: zoom-out;
}
</style>

<script>
export default {
    name: "ImageViewer",
    props: ["image", "beforeImage", "afterImage", "class", "fullscreen"],
    data() {
        const compare = this.beforeImage && this.afterImage ? true : false;
        return {
            image: this.image,
            beforeImage: this.beforeImage,
            afterImage: this.afterImage,
            compare: compare,
            fullscreen: this.fullscreen ? true : false,
            isModalVisible: false,
        };
    },
    methods: {
        show() {
            if (!this.fullscreen) return;
            this.isModalVisible = true;
            document.querySelector("body").style.overflow = "hidden";
            const img = document.querySelector(".fullscreen-img");
            if (img) {
                img.style.height = `${window.innerHeight}px`;
                img.style.width = "auto";
            }
        },
        close() {
            this.isModalVisible = false;
            document.querySelector("body").style.removeProperty("overflow");
        },
    },
};
</script>
