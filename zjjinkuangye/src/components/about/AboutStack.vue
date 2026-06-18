<template>
  <section class="about-stack">
    <div class="section-title-area">
      <h2>技术选型与数据字典</h2>
      <p>本平台前端采用模块化的 Vue 3 架构，数据采用自维护的结构化 JSON 规范，完全支持无后端的静态部署与交互。</p>
    </div>

    <div class="stack-grid">
      <!-- 技术选型卡 -->
      <div class="card stack-card">
        <h3>技术框架选型</h3>
        <div class="tech-list">
          <div class="tech-item">
            <strong>Vue 3</strong>
            <span>组合式 API (<code class="code-inline">&lt;script setup&gt;</code>) 编写响应式数据及组件联动逻辑。</span>
          </div>
          <div class="tech-item">
            <strong>Vite 7</strong>
            <span>新一代超快前端构建工具，提供极速的开发编译与热更新。</span>
          </div>
          <div class="tech-item">
            <strong>Vue Router 4</strong>
            <span>官方路由管理器，支撑 `/`、`/library`、`/keywords`、`/about` 等单页面应用路由分发。</span>
          </div>
          <div class="tech-item">
            <strong>Intersection Observer</strong>
            <span>浏览器原生 API，用以检测元素滚动进屏，触发高性能的平滑淡入渐显动画。</span>
          </div>
        </div>
      </div>

      <!-- 数据字典卡 -->
      <div class="card dict-card">
        <h3>合规文献 JSON 字段词典</h3>
        <div class="table-wrapper">
          <table class="dict-table">
            <thead>
              <tr>
                <th>属性字段 (Key)</th>
                <th>类型 (Type)</th>
                <th>描述及作用 (Description)</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="field in dictionary" :key="field.key">
                <td><code class="code-field">{{ field.key }}</code></td>
                <td><span class="type-badge">{{ field.type }}</span></td>
                <td>{{ field.desc }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const dictionary = [
  { key: 'id', type: 'Number', desc: '全局唯一样例记录唯一标识。' },
  { key: 'title', type: 'String', desc: '合规文献、新闻公告或法案政策标题。' },
  { key: 'sourceType', type: 'String', desc: '信源类型，如政策文件、法律法规、行业新闻、企业报告、国际规则。' },
  { key: 'region / country', type: 'String', desc: '文献涉及地域（如海南自贸港、欧盟）和国家（中国、多国等）。' },
  { key: 'businessStage', type: 'String', desc: '标记此文献所针对的跨境矿业运营业务阶段（总部布局、跨境结算等）。' },
  { key: 'category', type: 'String', desc: '政策合规主题二级类别（税收政策、关税贸易、数据跨境等）。' },
  { key: 'riskLevel', type: 'String', desc: '风险等级分类，定性为高风险、中风险、低风险。' },
  { key: 'keywords', type: 'Array[String]', desc: '从文本中清洗提取出的特征高频词，作为词云图与统计看板的数据来源。' },
  { key: 'summary / excerpt', type: 'String', desc: '重写的百字核心摘要与原文法条精选摘录。' },
  { key: 'analysis', type: 'String', desc: '针对紫金矿业业务场景撰写的结合性合规点评。' },
  { key: 'analysisResult', type: 'Object', desc: '包含 mainTopic（主题）、compliancePoints（要点）、riskReason（成因）、suggestion（应对建议）等深层标注明细。' }
]
</script>

<style scoped>
.about-stack {
  margin-bottom: clamp(24px, 4vw, 36px);
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

.stack-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: clamp(24px, 4vw, 36px);
}

@media (min-width: 1024px) {
  .stack-grid {
    grid-template-columns: 1fr 1.3fr;
  }
}

.card {
  padding: clamp(24px, 3.6vw, 36px);
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.06);
  background: linear-gradient(145deg, rgba(255, 255, 255, 0.025), rgba(255, 255, 255, 0.005)),
              rgba(16, 16, 16, 0.52);
  backdrop-filter: blur(14px);
  box-shadow: var(--shadow-deep);
}

h3 {
  font-size: 16px;
  font-weight: 950;
  margin: 0 0 20px;
  color: var(--color-gold, #c8a866);
  letter-spacing: 0.06em;
}

/* 技术栈 */
.tech-list {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.tech-item {
  display: flex;
  flex-direction: column;
  gap: 6px;
  border-top: 1px solid rgba(255, 255, 255, 0.04);
  padding-top: 14px;
}

.tech-item:first-child {
  border-top: none;
  padding-top: 0;
}

.tech-item strong {
  font-size: 14px;
  font-weight: 900;
  color: #ffffff;
}

.tech-item span {
  font-size: 13px;
  line-height: 1.6;
  color: var(--color-muted, #8e8e93);
}

.code-inline {
  font-family: monospace;
  background: rgba(255, 255, 255, 0.08);
  padding: 2px 4px;
  border-radius: 3px;
  color: #fff;
  font-size: 12px;
}

/* 表格样式 */
.table-wrapper {
  overflow-x: auto;
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: 6px;
  background: rgba(0, 0, 0, 0.2);
}

.dict-table {
  width: 100%;
  border-collapse: collapse;
  text-align: left;
  font-size: 13px;
}

.dict-table th,
.dict-table td {
  padding: 12px 16px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.04);
}

.dict-table th {
  background: rgba(255, 255, 255, 0.03);
  color: rgba(255, 255, 255, 0.6);
  font-weight: 900;
  text-transform: uppercase;
  font-size: 11px;
  letter-spacing: 0.08em;
}

.code-field {
  font-family: monospace;
  font-weight: 900;
  color: var(--color-gold, #c8a866);
}

.type-badge {
  font-family: monospace;
  background: rgba(255, 255, 255, 0.06);
  color: rgba(255, 255, 255, 0.8);
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 11px;
}

.dict-table td {
  color: var(--color-muted, #8e8e93);
  line-height: 1.55;
}

.dict-table tr:last-child td {
  border-bottom: none;
}
</style>
