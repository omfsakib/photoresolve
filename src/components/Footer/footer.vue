<script setup>
	import Logo from "@/components/icon/logo.vue";
	import NewsLaterVue from "@/components/pager/newslater.vue";
import axios from 'axios';
</script>
<template>
	<section class="section min-h-screen w-full inline-flex flex-col justify-end">
		<NewsLaterVue />
		<div class="bg-neutral-900 text-gray-200">
			<div
				class="px-4 pt-14 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8">
				<div
					class="grid gap-10 row-gap-6 mb-[5rem] sm:grid-cols-2 lg:grid-cols-4">
					<div class="sm:col-span-2">
						<div aria-label="Go home" title="photoresolve"
							class="inline-flex items-center text-white">
							<Logo />
							<span
								class="ml-2 text-xl font-normal tracking-wide uppercase">
								photo resolve
							</span>
						</div>
						<div class="mt-6 lg:max-w-sm">
							<p class="text-sm font-Montserrat"
								v-html="footer.description.text"></p>
						</div>
					</div>
					<div class="space-y-2 text-sm">
						<p class="text-base text-white font-black tracking-wide">
							Contact
						</p>
						<div class="flex" v-for="item in footer.contact"
							:aria-label="item.title" :title="item.title">
							<p v-if="item.value" class="mr-1" v-text="item.name"></p>
							<a :href="item.link" class="transition-colors duration-300"
								v-text="item.value"></a>
						</div>
					</div>
					<div>
						<span
							class="text-base text-white font-black tracking-wide">About</span>
						<p class="mt-1 text-sm font-Montserrat"
							v-html="footer.shortIntro.text"></p>
					</div>
				</div>
				<div
					class="flex flex-col-reverse justify-between pt-5 pb-5 border-t lg:flex-row">
					<p class="text-sm" v-html="
                            footer.copyRight.text
                                .replace('{{ years }}', years)
                                .replace('{{ domain }}', domain)
                        "></p>
					<ul
						class="flex flex-col mb-3 text-gray-100 space-y-2 lg:mb-0 sm:space-y-0 sm:space-x-5 sm:flex-row">
						<li v-for="item in footer.menu">
							<router-link :to="{ name: item.link }"
								class="text-sm transition-colors duration-300 hover:text-deep-purple-accent-400">
								{{ item.name }}
							</router-link>
						</li>
					</ul>
				</div>
			</div>
		</div>
	</section>
</template>

<script>
	export default {
		data() {
			return {
				footer: {
	description: {
	  text: '',
	},
	shortIntro: {
	  text: '',
	},
	copyRight: {
	  text: '© Copyright  {{ years }} | {{ domain }}',
	},
	contact: {
	  phone: {
		name: 'Phone:',
		title: 'Our Phone',
		value: '',
		link: '',
	  },
	  email: {
		name: 'Email:',
		title: 'Our Email',
		value: '',
		link: '',
	  },
	  address: {
		name: 'Address:',
		title: 'Our Address',
		value: '',
		link: '',
	  },
	},
	menu: [
	  {
		name: 'Privacy Policy',
		link: 'privacy-policy',
	  },
	  {
		name: 'Terms & Conditions',
		link: 'terms-and-conditions',
	  },
	],
},
			};
		},
		
		mounted() {
			axios.get('https://app.photoresolve.com/getFooterInfo/')
	.then(response => {
	this.footer.description.text = response.data.description;
	this.footer.shortIntro.text = response.data.shortIntro;
	this.footer.contact.phone.value = response.data.phone;
	this.footer.contact.phone.link = `tel:${response.data.phone}`;
	this.footer.contact.email.value = response.data.email;
	this.footer.contact.email.link = `mailto:${response.data.email}`;
	this.footer.contact.address.value = response.data.address;
	this.footer.contact.address.link = `https://www.google.com/maps?q=${response.data.address}`;
	})
	.catch(error => {
	console.error(error);
	})
    },
		computed: {
			years() {
				return new Date().getFullYear();
			},
			domain() {
				return this.$page.setting.domain;
			},
		},
	};
</script>