<script setup>
import { Dialog, DialogPanel, TransitionChild, TransitionRoot } from '@headlessui/vue'
</script>
<template>
	<TransitionRoot as="template" :show="isModalVisible">
		<Dialog as="div" class="relative z-10" @close="isModalVisible = false">
			<TransitionChild as="template" enter="ease-out duration-300"
				enter-from="opacity-0" enter-to="opacity-100" leave="ease-in duration-200"
				leave-from="opacity-100" leave-to="opacity-0">
				<div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
			</TransitionChild>

			<div
				style="cursor: pointer; position: fixed;z-index: 10000;top: 0;right: 0;background: #fff;border: 0;margin: 10px;padding: 1px 12px;border-radius: 3px;color: #000;">
				close</div>

			<div class="fixed inset-0 z-10 overflow-y-auto">
				<div
					class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
					<TransitionChild as="template" enter="ease-out duration-300"
						enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
						enter-to="opacity-100 translate-y-0 sm:scale-100"
						leave="ease-in duration-200"
						leave-from="opacity-100 translate-y-0 sm:scale-100"
						leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
						<DialogPanel
							class="relative transform overflow-hidden rounded-lg  shadow-xl transition-all  sm:max-w-lg md:max-w-none w-4/5">
							<video @contextmenu.prevent @click="toggle" ref="video"
								class="w-full aspect-video" src="@/assets/promot.mp4"
								autoplay></video>
						</DialogPanel>
					</TransitionChild>
				</div>
			</div>
		</Dialog>
	</TransitionRoot>
</template>
 
<script>
export default {
	name: 'Modal',
	setup() {
		this.$refs.video.controls = false;
	},
	data() {
		return {
			isModalVisible: true,
		};
	},
	methods: {
		close() {
			this.$emit('close');
		},
		toggle() {
			this.$refs.video.paused ? this.$refs.video.play() : this.$refs.video.pause();
		}
	},
};
</script>