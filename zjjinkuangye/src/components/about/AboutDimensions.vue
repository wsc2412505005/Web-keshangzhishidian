<template>
  <section class="about-dimensions">
    <div class="section-title-area">
      <h2>合规标注分类评估体系</h2>
      <p>为实现多视角的数据检索与深入剖析，平台对每条合规文献打上了三个维度的核心标签：</p>
    </div>

    <div class="dimension-tabs">
      <div
        v-for="tab in tabs"
        :key="tab.key"
        class="tab-card"
      >
        <div class="tab-card-header">
          <span class="dimension-icon">{{ tab.icon }}</span>
          <h3>{{ tab.title }}</h3>
        </div>
        <p class="tab-description">{{ tab.desc }}</p>
        
        <ul class="tag-list">
          <li v-for="tag in tab.tags" :key="tag.name">
            <span class="tag-label" :class="tag.class || ''">{{ tag.name }}</span>
            <span class="tag-desc">{{ tag.desc }}</span>
          </li>
        </ul>
      </div>
    </div>
  </section>
</template>

<script setup>
const tabs = [
  {
    key: 'risk',
    title: '风险等级划分 (Risk Levels)',
    icon: '🚨',
    desc: '基于政策约束力、行政处罚严重程度及跨国声誉受损度，划分三个定性评级：',
    tags: [
      { name: '高风险', class: 'tag-risk-high', desc: '涉及国际贸易制裁、冲突矿产尽调、跨国环境环保侵权等，一旦违规可能导致海外矿山项目直接停运或面临巨额诉讼。' },
      { name: '中风险', class: 'tag-risk-medium', desc: '涉及数据跨境出境安全评估、大额本外币外汇申报、海关保税加工增值账册核销等，违规会引发合规审核不通过与暂停运营。' },
      { name: '低风险', class: 'tag-risk-low', desc: '主要为支持鼓励性或总纲类规定，如自贸港 15% 企业所得税减免，只需满足常规性实质性运营认定即可享受优惠。' }
    ]
  },
  {
    key: 'stage',
    title: '跨境业务环节 (Business Stages)',
    icon: '⚡',
    desc: '对应矿业集团在海外扩张及海南三亚总部运营的八个核心阶段节点：',
    tags: [
      { name: '总部布局 / 投资设立', desc: '解释三亚国际运营平台的定位、注册登记及实质性运营要素。' },
      { name: '跨境结算 / 海外采购', desc: '涉及跨境本外币资金池运营、冲突矿产负责任供应链的合规尽调。' },
      { name: '供应链物流 / 海外贸易', desc: '如含进口有料件的关税免税申报、欧盟碳关税（CBAM）碳足迹填报。' },
      { name: '海外运营 / 数据合规', desc: '涵盖跨国生产运营的环境整治，以及企业内部敏感地理、地质数据出境自评。' }
    ]
  },
  {
    key: 'category',
    title: '合规分类主题 (Compliance Categories)',
    icon: '📁',
    desc: '针对文献涉及的内容范围，划分了七个具体的合规政策学科类别：',
    tags: [
      { name: '自贸港政策 / 税收政策', desc: '零关税、15%所得税等政策背景。' },
      { name: '关税与贸易 / 外汇与资金', desc: '进出口报关管理与一体化资金池结算。' },
      { name: '数据跨境 / 供应链尽调', desc: '重要业务数据出境以及供应商背景审查。' },
      { name: '环保与碳排放 / 环保合规', desc: '双碳政策、海外矿区社区关系维护及环境责任。' }
    ]
  }
]
</script>

<style scoped>
.about-dimensions {
  margin-bottom: clamp(48px, 7vw, 72px);
}

.section-title-area {
  margin-bottom: clamp(24px, 4vw, 36px);
}

.section-title-area h2 {
  font-size: clamp(20px, 2.4vw, 26px);
  font-weight: 900;
  margin: 0 0 8px;
  color: var(--color-text, #ffffff);
}

.section-title-area p {
  font-size: 14px;
  color: var(--color-muted, #8e8e93);
  margin: 0;
}

.dimension-tabs {
  display: grid;
  grid-template-columns: 1fr;
  gap: clamp(24px, 4vw, 36px);
}

@media (min-width: 1024px) {
  .dimension-tabs {
    grid-template-columns: 1fr 1fr;
  }
  .tab-card:first-child {
    grid-column: 1 / -1;
  }
}

.tab-card {
  padding: clamp(24px, 3.6vw, 36px);
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.06);
  background: linear-gradient(145deg, rgba(255, 255, 255, 0.025), rgba(255, 255, 255, 0.005)),
              rgba(16, 16, 16, 0.52);
  backdrop-filter: blur(14px);
  box-shadow: var(--shadow-deep);
}

.tab-card-header {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-bottom: 14px;
}

.dimension-icon {
  font-size: 22px;
}

.tab-card-header h3 {
  font-size: 16px;
  font-weight: 950;
  margin: 0;
  color: var(--color-gold, #c8a866);
  letter-spacing: 0.06em;
}

.tab-description {
  font-size: 13.5px;
  color: rgba(255, 255, 255, 0.7);
  margin: 0 0 20px;
  line-height: 1.6;
}

.tag-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.tag-list li {
  display: grid;
  grid-template-columns: 140px 1fr;
  gap: 16px;
  font-size: 13px;
  line-height: 1.6;
  border-top: 1px solid rgba(255, 255, 255, 0.04);
  padding-top: 14px;
}

.tag-list li:first-child {
  border-top: none;
  padding-top: 0;
}

.tag-label {
  justify-self: start;
  font-weight: 900;
  color: #ffffff;
  padding: 3px 10px;
  border-radius: 4px;
  background: rgba(255, 255, 255, 0.06);
  font-size: 12px;
  white-space: nowrap;
}

.tag-risk-high {
  color: #f0a08d;
  background: transparent;
  border: none;
  padding: 0;
}

.tag-risk-medium {
  color: #e2c581;
  background: transparent;
  border: none;
  padding: 0;
}

.tag-risk-low {
  color: #93d0bd;
  background: transparent;
  border: none;
  padding: 0;
}

.tag-desc {
  color: var(--color-muted, #8e8e93);
}

@media (max-width: 600px) {
  .tag-list li {
    grid-template-columns: 1fr;
    gap: 6px;
  }
}
</style>
