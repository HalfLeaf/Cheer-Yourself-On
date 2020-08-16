<template>
    <v-carousel height="100%" class="carousel-cheer-on" delimiter-icon="mdi-minus"
      :cycle="true"
      :show-arrows="false"
      :interval="16000"
      @change="carouselChange"
    >
      <v-carousel-item
        v-for="(item,i) in items"
        :key="i"
        reverse-transition="fade-transition"
        transition="fade-transition"
      >
      <v-img :src="item.src" height="98%" width="99%">
        <template v-slot:content>
          <vue-typed-js :strings="item | cookTyped"	:loopCount="32" :attr="'placeholder'">
            <h1 class="typing"></h1>
          </vue-typed-js>
        </template>
      </v-img>
      </v-carousel-item>
  </v-carousel>
</template>

<script>
import VueTypedJs from 'vue-typed-js';
const jinrishici = require('jinrishici');

export default {
  name:"cheer-on",
  components: {
    VueTypedJs
  },
  data() {
    return {
      defaultImg:"https://pixabay.com/zh/images/download/nepal-2184940_1920.jpg",
      imgList:[],
      total:1,
      items: [],
      jinrishiciData:{},
    }
  },
  filters: {
    cookTyped(item){
      return [item.title, item.author, ...item.content]
    }
  },
  methods: {
    getData(){
      let _this = this;
      jinrishici.load(res => {
        this.jinrishiciData = res.data;
      });
    },
    async getImageData(query){
      let origin = this.jinrishiciData.origin;
      await this.$axios.get("https://pixabay.com/api/?page=1&per_page=20&key=17387491-6065a6ba72bb2744536566c1d&lang=zh&q="+query).then(resp => {
        this.imgList = resp.data.hits;
        this.total = this.imgList.length > 20 ? 20:this.imgList.length;
        let i = parseInt(Math.random()*this.total);
        let image = "";
        try {
          image = this.imgList[i].webformatURL
        } catch (error) {
          image = this.defaultImg;
        }
        this.items.push({
          content:origin.content,
          author:origin.author,
          title:origin.title,
          src:image
        })
        this.getLoveTalk();
        this.getHitokotoData();
      });
    },
    async getLoveTalk(){
      let _this = this;
      let loveTalk = await require("./loveTalk.js").default;
      let index = parseInt(Math.random()*1291);
      let k = parseInt(Math.random()*_this.total);
      let img = "";
      try {
        img = _this.imgList[k].webformatURL;
      } catch (error) {
        img = _this.defaultImg;
      }
      _this.items.push({
        content:loveTalk[index],
        author:"",
        title:"我想对你说~",
        src:img
      })
    },
    async getHitokotoData(){
      let _this = this;
      await this.$axios.get('https://v1.hitokoto.cn/?encode=json&c=f&c=j&c=h&c=d&c=l').then(response => {
        let hitokotoContent = response.data.hitokoto;
        let hitokotoFrom = response.data.from;
        let content = [hitokotoContent];
        let j = parseInt(Math.random()*_this.total);
        let img = "";
        try {
          img = _this.imgList[j].webformatURL
        } catch (error) {
          img = _this.defaultImg;
        }
        _this.items.push({
          content:content,
          author:hitokotoFrom,
          title:"",
          src:img
        })
      })
    },
    carouselChange(value){
      let item = this.items[value];
      // var typed = new Typed('#word', {
      //   strings: [item.title, item.author, ...item.content],
      //   typeSpeed: 30
      // });
    }
  },
  mounted() {
    this.getData();
  },
  watch:{
    jinrishiciData(val){
      if(!val) return;
      let tags = val.matchTags;
      let query = tags.length>1?tags[1]:tags.join("+");
      this.getImageData(query);
    }
  }
}
</script>

<style lang="stylus" scoped>
.carousel-cheer-on
  left  0
  right 0
  top 0
  bottom 0
  height 100%
  width  100%
  position absolute
.shici-word
  color #64FFDA
  font-size 16px
  font-weight 700
  top 36%
  position relative
  
</style>