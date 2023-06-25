<!-- <script setup>
import IconPlus from "@/components/icon/plus.vue";
import IconMinus from "@/components/icon/minus.vue";
</script>
<template>
    <div class="bg-white dark:bg-gray-900">
        <div class="mx-auto max-w-full md:max-w-full lg:max-w-screen-lg">
            <div class="container px-6 py-10 mx-auto">
                <h1 class="text-3xl text-left font-semibold text-gray-800 dark:text-white">
                    Client's Frequently asked questions.
                </h1>

                <hr class="my-6 border-gray-200 dark:border-gray-700" />

                <div>
                    <div v-for="item in faq" :key="item.id">
                        <button
                            class="flex items-center focus:outline-none btn-faq"
                            aria-expanded="false"
                        >
                            <IconPlus
                                class="flex-shrink-0 w-6 h-6 text-blue-500 iconPlus"
                            />
                            <IconMinus
                                class="flex-shrink-0 w-6 h-6 text-blue-500 iconMinus"
                            />

                            <h1
                                class="mx-4 text-left text-[18px] sm:text-xl text-gray-700 dark:text-white"
                                v-text="item.name"
                            ></h1>
                        </button>

                        <div class="flex md:mx-10 content">
                            <span class="border border-blue-500"></span>

                            <p
                                class="max-w-3xl text-left px-4 mt-1 text-gray-500 dark:text-gray-300"
                                v-text="item.content"
                            ></p>
                        </div>

                        <hr class="my-8 border-gray-200 dark:border-gray-700" />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data: () => ({
        faq: [
            {
                name: "What’s our capability to do clipping paths in a day ?",
                content:
                    "We have 50 hand draw brilliant and dedicated clipping paths staffs and they can easily do at least 1000 images in a day without any hesitation.",
            },
            {
                name: "Do you announce any offer for a large volume of images for liquefying photoshop?",
                content:
                    "Yes, we do announce an offer for large amount images. Discounts depend on your quantity of photos",
            },
            {
                name: "Do you have a discount price for bulk image Color Correction Services?",
                content:
                    "Yeah we discount on bulk images orders from our clients. By discussing your volume of an image we will make a decision.",
            },
            {
                name: "Which types of Image Masking Services do you offer?",
                content:
                    "we provide numerous types of image masking services.Those are hair &fur,color,translucent,transparent,object masking etc",
            },
            {
                name: "What’s your payment getway?",
                content:
                    "We do accept 200 payment getway.Paypal,payoneer,visa card,master card and any other of them",
            },
            {
                name: "Who needs clipping paths services",
                content:
                    "Actually, e-commerce, Various types of photographers, Retail Business owners, Media, Ads agency and few other companies who are attached with image business, they need this service. For making up a photo properly clipping paths is needed very much.",
            },
            {
                name: "Have we any offer for a free trial service?",
                content:
                    "Obviously we offer a free trial service to our clients that they can understand how capable we are. After that, if they will satisfy then we will start to do work with them.",
            },
            {
                name: "Whom This Service For and why you are best?",
                content:
                    ": Mainly Professional Photographers, E-commerce businesses owner, Model agencies, Magazine companies who need to present their images to their clients and who need these photos to be eye-catching for promotional purposes they need this service badly. By knowing what our clients want and our extraordinary retouching team is experienced and skilled. For this, we believe we are the best provider",
            },
        ],
    }),
    mounted() {
        const items = document.querySelectorAll("button.btn-faq");

        function toggleAccordion() {
            const itemToggle = this.getAttribute("aria-expanded");

            for (let i = 0; i < items.length; i++) {
                items[i].setAttribute("aria-expanded", "false");
            }

            if (itemToggle == "false") {
                this.setAttribute("aria-expanded", "true");
            }
        }

        items.forEach((item) => item.addEventListener("click", toggleAccordion));
    },
};
</script> -->
