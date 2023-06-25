<template>
	<section class="relative flex bg-white dark:bg-gray-900">
		<div
			class="flex flex-col justify-center mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl px-4 py-10">
			<h1
				class="text-3xl font-semibold text-gray-800 capitalize lg:text-4xl xl:text-5xl dark:text-white">
				What our <span class="text-blue-500">customers</span> <br> are saying
			</h1>

			<carousel class="
					grid 
					w-full  
				" :settings="settings" :breakpoints="breakpoints" :items-to-show="2.9"
				:wrap-around="false">
				<slide class="
						bg-white 
						dark:bg-gray-800
						w-full
						p-6 
						!m-6
						rounded-md 
						shadow-lg 
						text-left
					" v-for="testimonial in testimonials" :key="testimonial">
					<div class="carousel__item">
						<p class="leading-loose text-gray-500 dark:text-gray-400"
							v-text="testimonial.content"></p>

						<div class="flex items-center mt-2 -mx-2"
							v-if="testimonial.author">
							<img class="object-cover mx-2 rounded-full w-9 h-9"
								:src="testimonial.author.image">

							<div class="mx-1">
								<h1 class="font-normal text-gray-800 dark:text-white"
									v-text="testimonial.author.name"></h1>
								<span class="text-sm text-gray-500 dark:text-gray-400"
									v-text="testimonial.author.role"></span>
							</div>
						</div>
					</div>
				</slide>

			</carousel>

		</div>
	</section>
</template>
<style>
.carousel__slide:first-child {
	margin-left: 5.5px !important;
}
</style> 

<script>
// If you are using PurgeCSS, make sure to whitelist the carousel CSS classes
import 'vue3-carousel/dist/carousel.css';
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel';

export default {
	name: 'App',
	components: {
		Carousel,
		Slide,
		Pagination,
		Navigation,
	},
	data() {
		return {

			// carousel settings
			settings: {
				itemsToShow: 1,
				snapAlign: 'left',
			},
			// breakpoints are mobile first
			// any settings not specified will fallback to the carousel settings
			breakpoints: {
				// 700px and up
				768: {
					itemsToShow: 2.5,
					snapAlign: 'center',
				},
				// 1024 and up
				1024: {
					itemsToShow: 3,
					snapAlign: 'left',
				},
				// 1024 and up
				1536: {
					itemsToShow: 4.9,
					snapAlign: 'start',
				}
			},

			testimonials: [
				{
					id: 1,
					content: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Sit ea tempora dolores qui eius pariatur odit ad voluptas iste, cum accusantium beatae tempore quasi nesciunt distinctio.',
					author: {
						name: 'Robbert',
						role: 'CTO, Robert Consultency',
						image: 'https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80'
					}
				},
				{
					id: 2,
					content: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Sit ea tempora dolores qui eius pariatur odit ad voluptas iste, cum accusantium beatae tempore quasi nesciunt distinctio.',
					author: {
						name: 'Robbert',
						role: 'CTO, Robert Consultency',
						image: 'https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80'
					}
				},
				{
					id: 2,
					content: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Sit ea tempora dolores qui eius pariatur odit ad voluptas iste, cum accusantium beatae tempore quasi nesciunt distinctio.',
					author: {
						name: 'Robbert',
						role: 'CTO, Robert Consultency',
						image: 'https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80'
					}
				},
				{
					id: 2,
					content: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Sit ea tempora dolores qui eius pariatur odit ad voluptas iste, cum accusantium beatae tempore quasi nesciunt distinctio.',
					author: {
						name: 'Robbert',
						role: 'CTO, Robert Consultency',
						image: 'https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80'
					}
				},
				{
					id: 2,
					content: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Sit ea tempora dolores qui eius pariatur odit ad voluptas iste, cum accusantium beatae tempore quasi nesciunt distinctio.',
					author: {
						name: 'Robbert',
						role: 'CTO, Robert Consultency',
						image: 'https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80'
					}
				},
				{
					id: 2,
					content: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Sit ea tempora dolores qui eius pariatur odit ad voluptas iste, cum accusantium beatae tempore quasi nesciunt distinctio.',
					author: {
						name: 'Robbert',
						role: 'CTO, Robert Consultency',
						image: 'https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80'
					}
				},
				{
					id: 2,
					content: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Sit ea tempora dolores qui eius pariatur odit ad voluptas iste, cum accusantium beatae tempore quasi nesciunt distinctio.',
					author: {
						name: 'Robbert',
						role: 'CTO, Robert Consultency',
						image: 'https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80'
					}
				},
				{
					id: 2,
					content: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Sit ea tempora dolores qui eius pariatur odit ad voluptas iste, cum accusantium beatae tempore quasi nesciunt distinctio.',
					author: {
						name: 'Robbert',
						role: 'CTO, Robert Consultency',
						image: 'https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80'
					}
				},
				{
					id: 2,
					content: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Sit ea tempora dolores qui eius pariatur odit ad voluptas iste, cum accusantium beatae tempore quasi nesciunt distinctio.',
					author: {
						name: 'Robbert',
						role: 'CTO, Robert Consultency',
						image: 'https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80'
					}
				},
				{
					id: 2,
					content: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Sit ea tempora dolores qui eius pariatur odit ad voluptas iste, cum accusantium beatae tempore quasi nesciunt distinctio.',
					author: {
						name: 'Robbert',
						role: 'CTO, Robert Consultency',
						image: 'https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80'
					}
				}
			],
		}
	}
};
</script>