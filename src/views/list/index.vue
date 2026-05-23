<template>
  <div class="list-page">
    <div class="list-page__header">
      <h1 class="list-page__title">数据列表</h1>
      <el-button type="primary" @click="handleAdd">
        <el-icon><Plus /></el-icon>
        新增
      </el-button>
    </div>
    
    <div class="list-page__content">
      <div class="list-page__toolbar">
        <div class="list-page__search">
          <el-input
            v-model="searchKeyword"
            placeholder="请输入名称搜索"
            clearable
            style="width: 240px"
            @clear="handleSearch"
            @keyup.enter="handleSearch"
          >
            <template #prefix>
              <el-icon><Search /></el-icon>
            </template>
          </el-input>
          <el-button type="primary" @click="handleSearch">
            搜索
          </el-button>
          <el-button @click="handleReset">
            重置
          </el-button>
        </div>
      </div>
      
      <el-table
        v-loading="loading"
        :data="tableData"
        stripe
        border
        style="width: 100%"
        @sort-change="handleSortChange"
      >
        <el-table-column
          prop="name"
          label="名字"
          min-width="180"
          sortable="custom"
          show-overflow-tooltip
        >
          <template #default="{ row }">
            <span class="name-cell">{{ row.name }}</span>
          </template>
        </el-table-column>
        
        <el-table-column
          prop="createdAt"
          label="生成时间"
          min-width="180"
          sortable="custom"
          align="center"
        >
          <template #default="{ row }">
            <span class="time-cell">{{ formatDate(row.createdAt) }}</span>
          </template>
        </el-table-column>
        
        <el-table-column
          label="操作"
          width="180"
          align="center"
          fixed="right"
        >
          <template #default="{ row }">
            <el-button
              type="primary"
              link
              @click="handleView(row)"
            >
              查看
            </el-button>
            <el-button
              type="primary"
              link
              @click="handleEdit(row)"
            >
              编辑
            </el-button>
            <el-button
              type="danger"
              link
              @click="handleDelete(row)"
            >
              删除
            </el-button>
          </template>
        </el-table-column>
      </el-table>
      
      <div class="list-page__pagination">
        <el-pagination
          v-model:current-page="pagination.currentPage"
          v-model:page-size="pagination.pageSize"
          :page-sizes="[10, 20, 50, 100]"
          :total="pagination.total"
          layout="total, sizes, prev, pager, next, jumper"
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import type { ListItem, Pagination } from '@/types'
import { formatDate } from '@/utils/format'

const loading = ref(false)
const searchKeyword = ref('')

const tableData = ref<ListItem[]>([])

const pagination = reactive<Pagination>({
  currentPage: 1,
  pageSize: 10,
  total: 0
})

const sortParams = reactive({
  prop: '',
  order: ''
})

const mockData: ListItem[] = Array.from({ length: 50 }, (_, index) => ({
  id: `${index + 1}`,
  name: `项目 ${String(index + 1).padStart(3, '0')}`,
  createdAt: new Date(Date.now() - Math.random() * 30 * 24 * 60 * 60 * 1000).toISOString()
}))

const fetchData = async () => {
  loading.value = true
  
  try {
    await new Promise(resolve => setTimeout(resolve, 500))
    
    let filteredData = [...mockData]
    
    if (searchKeyword.value) {
      filteredData = filteredData.filter(item =>
        item.name.toLowerCase().includes(searchKeyword.value.toLowerCase())
      )
    }
    
    if (sortParams.prop && sortParams.order) {
      filteredData.sort((a, b) => {
        const aVal = a[sortParams.prop as keyof ListItem]
        const bVal = b[sortParams.prop as keyof ListItem]
        
        if (sortParams.order === 'ascending') {
          return aVal > bVal ? 1 : -1
        } else {
          return aVal < bVal ? 1 : -1
        }
      })
    }
    
    pagination.total = filteredData.length
    
    const start = (pagination.currentPage - 1) * pagination.pageSize
    const end = start + pagination.pageSize
    tableData.value = filteredData.slice(start, end)
    
  } finally {
    loading.value = false
  }
}

const handleSearch = () => {
  pagination.currentPage = 1
  fetchData()
}

const handleReset = () => {
  searchKeyword.value = ''
  pagination.currentPage = 1
  fetchData()
}

const handleSortChange = ({ prop, order }: { prop: string; order: string }) => {
  sortParams.prop = prop
  sortParams.order = order
  fetchData()
}

const handleSizeChange = (size: number) => {
  pagination.pageSize = size
  pagination.currentPage = 1
  fetchData()
}

const handleCurrentChange = (page: number) => {
  pagination.currentPage = page
  fetchData()
}

const handleAdd = () => {
  ElMessage.info('新增功能待实现')
}

const handleView = (row: ListItem) => {
  ElMessage.info(`查看：${row.name}`)
}

const handleEdit = (row: ListItem) => {
  ElMessage.info(`编辑：${row.name}`)
}

const handleDelete = (row: ListItem) => {
  ElMessageBox.confirm(
    `确定要删除 "${row.name}" 吗？`,
    '删除确认',
    {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning'
    }
  ).then(() => {
    ElMessage.success('删除成功')
    fetchData()
  }).catch(() => {
    ElMessage.info('已取消删除')
  })
}

onMounted(() => {
  fetchData()
})
</script>

<style lang="scss" scoped>
@import '@/styles/components/list.scss';

.name-cell {
  font-weight: 500;
  color: #409EFF;
}

.time-cell {
  color: #909399;
  font-size: 13px;
}
</style>
