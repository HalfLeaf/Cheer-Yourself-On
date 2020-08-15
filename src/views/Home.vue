<template>
  <vueper-slides class="slide-div" :autoplay="true" :3d="true" :duration="9000">
    <vueper-slide v-for="(slide, i) in slides" :key="i" :title="slide.title" :style="{background: defaultImg}">
      <template v-slot:content>
        <mymarquee :lists="slide.content" class="slide-marquee"></mymarquee>
      </template>
    </vueper-slide >
  </vueper-slides>
</template>


<script>
import DATA from "./loveTalk.js"
import mymarquee from './my-marquee';
import { createClient } from 'pexels';
import { VueperSlides, VueperSlide } from 'vueperslides'
import 'vueperslides/dist/vueperslides.css'
const jinrishici = require('jinrishici');
const pexelsClient = createClient('563492ad6f91700001000001a4c9a33ce81b4164b6c2a3a5a92383bb');

export default {
  name: 'Home',
  components: {
    VueperSlides,
    VueperSlide,
    mymarquee
  },
  data(){
    return{
      DATA,
      imgList:[],
      currentImg:"",
      defaultImg:"https://pixabay.com/get/54e5dd474850ae14f1dc84609629307d1d38daec524c704c7c2972dc944cc450_640.jpg",
      hitokotoContent:"",
      hitokotoFrom:"",
      slides: [],
    }
  },
  methods: {
    getJsonFile(){
      let _this = this;
      jinrishici.load(res => {
        let data = res.data;
        let tags = data.matchTags;
        let query = tags.length>1?tags[1]:tags.join("+");
        this.$axios.get("https://pixabay.com/api/?page=1&per_page=10&key=17387491-6065a6ba72bb2744536566c1d&lang=zh&q="+query).then(resp => {
          this.imgList = resp.data.hits;
          this.currentImg = this.imgList.length >0?this.imgList[0].webformatURL:this.defaultImg;
          this.slides.push({title:data.origin.title, content:data.origin.content, image:this.currentImg})
        });
      });
      this.$axios.get('https://v1.hitokoto.cn/?encode=json&c=f&c=j&c=h&c=d&c=l').then(response => {
        this.hitokotoContent = response.data.hitokoto;
        this.hitokotoFrom = response.data.from;
        let content = this.hitokotoContent.split(",");
        content.push(" ");
        content.push(" ");
        content.push(" ");
        this.slides.push({title:this.hitokotoFrom, content:content, image:this.currentImg})
      })
      let index = parseInt(Math.random()*1291); 
      this.slides.push({title:"我想对你说~", content:this.DATA[""+index], image:this.currentImg})

    }
  },
  mounted(){
    this.getJsonFile();
  }
}
</script>

<style lang="stylus" scoped>
.slide-div
  height 100%
  weight 100%
  left 0
  right 0
  bottom 0
  top 0
  position absolute

.slide-marquee
  left 5%
  top 32%
  position relative
</style>
