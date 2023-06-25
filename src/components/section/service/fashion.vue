<script setup>
import CardWrapper from "../../utility/cardWrapper.vue";
import HeaderContent from "./HeaderContent.vue";
import axios from 'axios';
import HowITWorkVue from '../../pager/how-it-work.vue'
</script>
<template>
    <full-page ref="fullpage" :options="options">
        <section class="section">
            <Header />
            <HeaderContent :title="service.title" :content="service.content" :image="service.after"
                :featureList="service.featureList" />
        </section>
        <CardWrapper :setdata="service.sub_services1" />
        <CardWrapper :setdata="service.sub_services2" />
        <HowITWorkVue />
        <Footer />
    </full-page>
</template>

<script>
export default {
    data() {
        return {
            service: [],
            options: {
                licenseKey: "gplv3-license",
                responsiveWidth: 800,
                navigation: false,
                anchors: ['first', 'second', 'third'],

                // other options
            },
        };
    },
    methods: {
        fetchPosts() {
            axios.get('https://app.photoresolve.com/getService/E-Commerce & Model Retouch')
                .then(response => {
                    this.service = response.data;
                    console.log(response.data)
                })
                .catch(error => {
                    console.error(error);
                });
        }
    },
    mounted() {
        this.fetchPosts();
        this.$refs.fullpage.api.silentMoveTo('first', 1);
    }
};
</script>
