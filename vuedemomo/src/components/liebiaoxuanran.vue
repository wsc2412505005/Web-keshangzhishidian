<template>
  <div class="liebiaoxuanran">
    <h3>列表渲染</h3>
    <div v-for="value in names">{{value}}</div>
    <div v-for="(value1, index) in names">{{value1}}----{{index}}</div>
    <div v-for="(item, index) in results" :key="index">
      <p>{{item.name}}</p>
      <img :src="item.img" :alt="item.title" />
    </div>
    <div v-for="(value, key, index) in myObject">{{value}}---{{key}}---{{index}}</div>
    <hr>
  </div>
</template>

<script>
export default {
  name: "4liebiaoxuanran",
  data() {
    return {
      names: ["zhangsan", "lisi", "wangwu"],
      results: [
        {
            "gkey": "tzcqol",
            "img": "//p0.qhimg.com/t11098f6bcdf05cf5f5a4719717.gif",
            "w64": -1,
            "gdata": "{\"type\":\"webgame\",\"title\":\"天尊传奇\",\"iconid\":4160342,\"url\":\"http:\\/\\/v5.360game.360.cn\\/zones?gkey=tzcqol\",\"openUrl\":\"http:\\/\\/v5.360game.360.cn\\/zones?gkey=tzcqol\",\"fold\":\"1\",\"icon\":\"http:\\/\\/p0.qhimg.com\\/t11098f6bcdaded4bee5a270774.png\",\"gkey\":\"tzcqol\"}",
            "qcmsint1": "0",
            "gtype": "1",
            "title": "天尊传奇",
            "bigbrief": "天尊传奇",
            "url": "http://v5.360game.360.cn/zones?gkey=tzcqol",
            "brief": "九大特色职业",
            "ten": "0",
            "name": "天尊传奇"
        },
        {
            "gkey": "zsdl",
            "img": "//p0.qhimg.com/t11098f6bcd4a8e7b6755dfc822.gif",
            "w64": -1,
            "gdata": "{\"type\":\"webgame\",\"title\":\"众神大陆\",\"iconid\":4232232,\"url\":\"http:\\/\\/v5.360game.360.cn\\/zones?gkey=zsdl\",\"openUrl\":\"http:\\/\\/v5.360game.360.cn\\/zones?gkey=zsdl\",\"fold\":\"1\",\"icon\":\"http:\\/\\/p0.qhimg.com\\/t11098f6bcdcd9c01cb18cae422.png\",\"gkey\":\"zsdl\"}",
            "qcmsint1": "0",
            "gtype": "1",
            "title": "众神大陆",
            "bigbrief": "众神大陆",
            "url": "http://v5.360game.360.cn/zones?gkey=zsdl",
            "brief": "经典重现 再战天下",
            "ten": "0",
            "name": "众神大陆"
        },
        {
            "gkey": "hhxxlol",
            "img": "//p0.qhimg.com/t11098f6bcda51a81297e49a5c2.png",
            "w64": -1,
            "gdata": "{\"type\":\"webgame\",\"title\":\"洪荒西行录\",\"iconid\":4163982,\"url\":\"http:\\/\\/v5.360game.360.cn\\/zones?gkey=hhxxlol\",\"openUrl\":\"http:\\/\\/v5.360game.360.cn\\/zones?gkey=hhxxlol\",\"fold\":\"1\",\"icon\":\"http:\\/\\/p0.qhimg.com\\/t11098f6bcd64a7566dfa22cc00.png\",\"gkey\":\"hhxxlol\"}",
            "qcmsint1": "0",
            "gtype": "1",
            "title": "洪荒西行录",
            "bigbrief": "洪荒西行录",
            "url": "http://v5.360game.360.cn/zones?gkey=hhxxlol",
            "brief": "0.1折西行重启",
            "ten": "0",
            "name": "洪荒西行录"
        },
        {
            "gkey": "djxzbdol",
            "img": "//p1.qhimg.com/t11d60b18a2fbbb12fe3227d17b.gif",
            "w64": -1,
            "gdata": "{\"type\":\"webgame\",\"title\":\"刀剑笑之霸刀\",\"iconid\":4073502,\"url\":\"http:\\/\\/v5.360game.360.cn\\/zones?gkey=djxzbdol\",\"openUrl\":\"http:\\/\\/v5.360game.360.cn\\/zones?gkey=djxzbdol\",\"fold\":\"1\",\"icon\":\"http:\\/\\/p0.qhimg.com\\/t11098f6bcd2e3acb346573f3d5.png\",\"gkey\":\"djxzbdol\"}",
            "qcmsint1": "0",
            "gtype": "1",
            "title": "刀剑笑之霸刀",
            "bigbrief": "刀剑笑之霸刀",
            "url": "http://v5.360game.360.cn/zones?gkey=djxzbdol",
            "brief": "双职业超变高燃",
            "ten": "0",
            "name": "刀剑笑之霸刀"
        },
      ],
      myObject: {
        title: 'how to do in vue',
        author: 'aaa',
        publishshin: '2026-04-10'
      }
    };
  }
};
</script>

<style scoped>
.liebiaoxuanran {
  color: chocolate;
}
</style>
