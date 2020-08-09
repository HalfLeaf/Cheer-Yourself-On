<template>
  <div>
    <vs-navbar
      v-model="activeItem" 
      class="nabarx"
      type="flat"
      color="success"
      text-color="rgba(255,255,255,.6)"
      active-text-color="rgba(255,255,255,1)">
      <div slot="title">
        <vs-navbar-title>
          一诗 · 一词 · 一图 · 一茗 · 一成长 
        </vs-navbar-title>
      </div>
      <vs-navbar-item index="0">诗词</vs-navbar-item>
      <vs-navbar-item index="1">美图</vs-navbar-item>
      <vs-navbar-item index="2">情话</vs-navbar-item>
    </vs-navbar>
    <vueper-slides>
      <vueper-slide v-for="(slide, i) in slides" :key="i" :title="slide.title" :content="slide.content" />
    </vueper-slides>
  </div>
</template>


<script>
import { createClient } from 'pexels';
import { VueperSlides, VueperSlide } from 'vueperslides'
import 'vueperslides/dist/vueperslides.css'
const jinrishici = require('jinrishici');
const pexelsClient = createClient('563492ad6f91700001000001a4c9a33ce81b4164b6c2a3a5a92383bb');

export default {
  name: 'Home',
  components: {
    VueperSlides,
    VueperSlide 
    
  },
  data(){
    return{
      imgList:[],
      currentImg:"",
      defaultImg:"https://pixabay.com/get/54e5dd474850ae14f1dc84609629307d1d38daec524c704c7c2972dc944cc450_640.jpg",
      slides: [
        {
          title: 'Slide #1',
          content: 'Slide content.'
        }
      ]
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
          console.log(resp)
          this.imgList = resp.data.hits;
          this.currentImg = this.imgList.length >0?this.imgList[0].webformatURL:this.defaultImg;
        });
      });
      this.$axios.get('https://v1.hitokoto.cn/?encode=json').then(response => {

      })

    }
  },
  mounted(){
    this.getJsonFile();
  }
}
</script>
