<template>
            <div v-if="showPopup" class="popup-overlay">
                <div class="popup-content">
                  <div class="image-container">
                      <img :src="imageAfter" class="object-contain max-h-screen image-after slider-image">
                      <img :src="imageBefore" class="object-contain max-h-screen image-before slider-image">
                      <button class="popup-close" @click="showPopup = false">×</button>
                  </div>
                  <input type="range" min="0" max="100" class="slider" aria-label="Percentage of before photo shown" v-model="sliderValue" @input="handleSliderChange">
                  <div class="slider-line"></div>
                  <div class="slider-button" aria-hidden="true">
                      <svg
      xmlns="http://www.w3.org/2000/svg"
      width="30"
      height="30"
      fill="currentColor"
      viewBox="0 0 256 256"
    >
      <rect width="256" height="256" fill="none"></rect>
      <line
        x1="128"
        y1="40"
        x2="128"
        y2="216"
        fill="none"
        stroke="currentColor"
        stroke-linecap="round"
        stroke-linejoin="round"
        stroke-width="16"
      ></line>
      <line
        x1="96"
        y1="128"
        x2="16"
        y2="128"
        fill="none"
        stroke="currentColor"
        stroke-linecap="round"
        stroke-linejoin="round"
        stroke-width="16"
      ></line>
      <polyline
        points="48 160 16 128 48 96"
        fill="none"
        stroke="currentColor"
        stroke-linecap="round"
        stroke-linejoin="round"
        stroke-width="16"
      ></polyline>
      <line
        x1="160"
        y1="128"
        x2="240"
        y2="128"
        fill="none"
        stroke="currentColor"
        stroke-linecap="round"
        stroke-linejoin="round"
        stroke-width="16"
      ></line>
      <polyline
        points="208 96 240 128 208 160"
        fill="none"
        stroke="currentColor"
        stroke-linecap="round"
        stroke-linejoin="round"
        stroke-width="16"
      ></polyline>
    </svg>
                        
                        
                  </div>
                </div>
              </div>
    <div class="section">
        <section class="grid-section h-[100vh]">
            <article class="grid-area" v-for="item in setdata">
                <div aria-label="content" class="w-full">
                    <div class="p-10">
                        <div class="grid-content">
                            <div class="grid-title" v-html="item.title"></div>
                            <div
                                class="grid-content-description"
                                v-html="item.description"
                            ></div>
                            <div
                                class="mt-5 text-sm font-Montserrat font-semibold"
                                v-html="item.price"
                            ></div>
                            <div class="my-5">
                                <router-link
                                    :to="{ name: 'contact' }"
                                    class="grid-btn-round"
                                >
                                    Get a free quote
                                    <svg
                                        class="inline-block w-3 ml-1"
                                        fill="#fff"
                                        viewBox="0 0 12 12"
                                    >
                                        <path
                                            d="M9.707,5.293l-5-5A1,1,0,0,0,3.293,1.707L7.586,6,3.293,10.293a1,1,0,1,0,1.414,1.414l5-5A1,1,0,0,0,9.707,5.293Z"
                                        ></path>
                                    </svg>
                                </router-link>
                            </div>
                        </div>
                    </div>
                </div>

                <div aria-label="image" class="w-full">
                  <div class="grid-image-area">
                    <div class="grid-image" ref="myDiv">
                      <!-- display image if item.after is an image -->
                      <img v-if="isImage(item.after)" :src="item.after" @click="getImageSrc(item.after, item.before)" />
                
                      <!-- display video if item.after is a video -->
                      <video v-else-if="isVideo(item.after)" width="100%" height="auto" autoplay loop muted>
                        <source :src="item.after" type="video/mp4">
                      </video>
                    </div>
                  </div>
                </div>
            </article>
        </section>
    </div>
</template>

<script>
export default {
    props: ["setdata"],
    data() {
    return {
      showPopup: false,
      imageAfter:'',
      imageBefore:'',
      sliderValue: 50,
    }
  },
  computed: {
    position() {
      return `${this.sliderValue}%`;
    },
  },
  methods: {
    handleSliderChange(event) {
      const container = document.querySelector('.popup-content');
      container.style.setProperty('--position', `${event.target.value}%`);
    }, 
    isImage(url) {
        return /\.(jpeg|jpg|png|gif|webp)$/i.test(url)
    },  
    isVideo(url) {
        return /\.(mp4|mov|avi)$/i.test(url)
    },
      getImageSrc(after,before) {
        this.imageAfter = after
        this.imageBefore = before
        this.showPopup = true
        window.scrollTo({
      top: 0,
      behavior: "smooth"
    });
        // Do something with the image source
    }
  },
};
</script>
<style>
.popup-overlay {
  position: fixed;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
}
.max-h-screen {
  max-height: 85vh !important;
}
@media (max-width: 768px) {
  .popup-overlay {
    position: fixed;
    top:0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 9999;
  }
}
.grid-image video {
  height: 100%;
  width: 100%;
  -webkit-user-select: none;
  -moz-user-select: none;
  user-select: none;
  -o-object-fit: cover;
  object-fit: cover;
}
.popup-content {
  position: relative;
  max-width: 90%;
  max-height: 90%;
  background-color: white;
  border-radius: 5px;
  overflow: hidden;
  text-align: center;
  object-fit: contain;
  display: grid;
  place-content: center;
  --position: 50%;
}
.image-container{
    max-width: 100%;
    max-height: 100%;
}
.slider-image{
    width: 100%;
    height: 100%;
    background-color: #fff;
    object-fit: cover;
    object-position: left;
}
.image-before{
    position: absolute;
    inset: 0;
    width: var(--position);
}
.slider{
    position: absolute;
    inset: 0;
    cursor: pointer;
    opacity: 0;
    height: 100%;
    width: 100%;
}
.slider:focus-visible ~ .slider-button {
    outline: 5px solid black;
    outline-offset: 3px;
  }
.slider-line{
    position: absolute;
    inset: 0;
    width: .2rem;
    height: 100%;
    background-color: #a8a8a8;
    z-index: 10;
    left: var(--position);
    transform: translateX(-50%);
    pointer-events: none;
}
.slider-button{
    position: absolute;
    background-color: #fff;
    color: black;
    padding: .5rem;
    top:38%;
    border-radius: 100vw;
    display: grid;
    place-items: center;
    left: var(--position);
    transform: translate(-50%, 50%);
    pointer-events: none;
    box-shadow: 1px 1px 1px hsl(0, 50%, 2%, .5);
    z-index: 10;
}
.popup-close {
  position: absolute;
  top: 10px;
  right: 10px;
  font-size: 24px;
  font-weight: bold;
  color: #999;
  cursor: pointer;
  z-index: 999;
  font-family: initial;
}
</style>