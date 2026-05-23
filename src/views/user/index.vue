<template>
  <div class="user-page">
    <div class="user-page__header">
      <h1 class="user-page__title">用户管理</h1>
      <div class="user-page__actions">
        <el-button type="primary" @click="handleAdd">
          <el-icon><Plus /></el-icon>
          新增用户
        </el-button>
      </div>
    </div>
    
    <div class="user-page__content">
      <div class="user-page__toolbar">
        <div class="user-page__search">
          <el-input
            v-model="searchForm.userName"
            placeholder="请输入用户名称搜索"
            clearable
            style="width: 240px"
          >
            <template #prefix>
              <el-icon><Search /></el-icon>
            </template>
          </el-input>
          
          <el-select
            v-model="searchForm.company"
            placeholder="请选择所属公司"
            clearable
            style="width: 180px"
          >
            <el-option
              v-for="company in companyOptions"
              :key="company.value"
              :label="company.label"
              :value="company.value"
            />
          </el-select>
          
          <el-select
            v-model="searchForm.industry"
            placeholder="请选择所属行业"
            clearable
            style="width: 180px"
          >
            <el-option
              v-for="industry in industryOptions"
              :key="industry.value"
              :label="industry.label"
              :value="industry.value"
            />
          </el-select>
          
          <el-date-picker
            v-model="searchForm.registerDate"
            type="daterange"
            range-separator="至"
            start-placeholder="开始日期"
            end-placeholder="结束日期"
            clearable
            style="width: 320px"
          />
          
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
        @selection-change="handleSelectionChange"
      >
        <el-table-column
          type="selection"
          width="55"
        />
        
        <el-table-column
          prop="userName"
          label="用户名称"
          min-width="150"
          show-overflow-tooltip
        />
        
        <el-table-column
          prop="company"
          label="所属公司"
          min-width="180"
          show-overflow-tooltip
        />
        
        <el-table-column
          prop="industry"
          label="所属行业"
          min-width="150"
          show-overflow-tooltip
        />
        
        <el-table-column
          prop="registerDate"
          label="注册日期"
          width="180"
          align="center"
        >
          <template #default="{ row }">
            <span>{{ formatDate(row.registerDate) }}</span>
          </template>
        </el-table-column>
        
        <el-table-column
          prop="level"
          label="用户等级"
          width="120"
          align="center"
        >
          <template #default="{ row }">
            <el-tag :type="getLevelType(row.level)">
              {{ row.level }}
            </el-tag>
          </template>
        </el-table-column>
        
        <el-table-column
          prop="status"
          label="用户状态"
          width="120"
          align="center"
        >
          <template #default="{ row }">
            <el-tag :type="row.status === '启用' ? 'success' : 'warning'">
              {{ row.status }}
            </el-tag>
          </template>
        </el-table-column>
        
        <el-table-column
          prop="updateDate"
          label="更新日期"
          width="180"
          align="center"
        >
          <template #default="{ row }">
            <span>{{ formatDate(row.updateDate) }}</span>
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
              :type="row.status === '启用' ? 'warning' : 'success'"
              link
              @click="handleToggleStatus(row)"
            >
              {{ row.status === '启用' ? '禁用' : '启用' }}
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
      
      <div class="user-page__pagination">
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
import { Plus, Search } from '@element-plus/icons-vue'
import { formatDate } from '@/utils/format'

interface User {
  id: string
  userName: string
  company: string
  industry: string
  registerDate: string
  level: string
  status: '启用' | '禁用'
  updateDate: string
}

interface Pagination {
  currentPage: number
  pageSize: number
  total: number
}

interface SearchForm {
  userName: string
  company: string
  industry: string
  registerDate: [Date | null, Date | null]
}

const loading = ref(false)
const selectedRows = ref<User[]>([])

const searchForm = reactive<SearchForm>({
  userName: '',
  company: '',
  industry: '',
  registerDate: [null, null]
})

const pagination = reactive<Pagination>({
  currentPage: 1,
  pageSize: 10,
  total: 0
})

const companyOptions = [
  { label: 'A公司', value: 'A公司' },
  { label: 'B公司', value: 'B公司' },
  { label: 'C公司', value: 'C公司' },
  { label: 'D公司', value: 'D公司' },
  { label: 'E公司', value: 'E公司' }
]

const industryOptions = [
  { label: '制造业', value: '制造业' },
  { label: '服务业', value: '服务业' },
  { label: '金融业', value: '金融业' },
  { label: '科技业', value: '科技业' },
  { label: '教育业', value: '教育业' }
]

const tableData = ref<User[]>([])

const levelTypes = {
  'VIP1': 'info',
  'VIP2': 'success',
  'VIP3': 'warning',
  'VIP4': 'danger',
  '普通用户': ''
}

const getLevelType = (level: string) => {
  return levelTypes[level as keyof typeof levelTypes] || ''
}

const mockData: User[] = Array.from({ length: 100 }, (_, index) => {
  const companies = ['A公司', 'B公司', 'C公司', 'D公司', 'E公司']
  const industries = ['制造业', '服务业', '金融业', '科技业', '教育业']
  const levels = ['普通用户', 'VIP1', 'VIP2', 'VIP3', 'VIP4']
  const statuses = ['启用', '禁用']
  
  return {
    id: `${index + 1}`,
    userName: `用户${String(index + 1).padStart(3, '0')}`,
    company: companies[Math.floor(Math.random() * companies.length)],
    industry: industries[Math.floor(Math.random() * industries.length)],
    registerDate: new Date(Date.now() - Math.random() * 365 * 24 * 60 * 60 * 1000).toISOString(),
    level: levels[Math.floor(Math.random() * levels.length)],
    status: statuses[Math.floor(Math.random() * statuses.length)] as '启用' | '禁用',
    updateDate: new Date(Date.now() - Math.random() * 30 * 24 * 60 * 60 * 1000).toISOString()
  }
})

const fetchData = async () => {
  loading.value = true
  
  try {
    await new Promise(resolve => setTimeout(resolve, 500))
    
    let filteredData = [...mockData]
    
    if (searchForm.userName) {
      filteredData = filteredData.filter(item =>
        item.userName.toLowerCase().includes(searchForm.userName.toLowerCase())
      )
    }
    
    if (searchForm.company) {
      filteredData = filteredData.filter(item =>
        item.company === searchForm.company
      )
    }
    
    if (searchForm.industry) {
      filteredData = filteredData.filter(item =>
        item.industry === searchForm.industry
      )
    }
    
    if (searchForm.registerDate[0] && searchForm.registerDate[1]) {
      const startDate = searchForm.registerDate[0].getTime()
      const endDate = searchForm.registerDate[1].getTime()
      
      filteredData = filteredData.filter(item => {
        const itemDate = new Date(item.registerDate).getTime()
        return itemDate >= startDate && itemDate <= endDate
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
  searchForm.userName = ''
  searchForm.company = ''
  searchForm.industry = ''
  searchForm.registerDate = [null, null]
  pagination.currentPage = 1
  fetchData()
}

const handleSelectionChange = (selection: User[]) => {
  selectedRows.value = selection
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
  ElMessage.info('新增用户功能待实现')
}

const handleView = (row: User) => {
  ElMessage.info(`查看用户：${row.userName}`)
}

const handleEdit = (row: User) => {
  ElMessage.info(`编辑用户：${row.userName}`)
}

const handleToggleStatus = (row: User) => {
  const newStatus = row.status === '启用' ? '禁用' : '启用'
  ElMessageBox.confirm(
    `确定要${newStatus}用户 "${row.userName}" 吗？`,
    '状态变更确认',
    {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning'
    }
  ).then(() => {
    row.status = newStatus as '启用' | '禁用'
    ElMessage.success(`${newStatus}成功`)
  }).catch(() => {
    ElMessage.info('已取消操作')
  })
}

const handleDelete = (row: User) => {
  ElMessageBox.confirm(
    `确定要删除用户 "${row.userName}" 吗？`,
    '删除确认',
    {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning'
    }
  ).then(() => {
    // 在实际项目中，这里应该调用API删除数据
    const index = tableData.value.findIndex(item => item.id === row.id)
    if (index > -1) {
      tableData.value.splice(index, 1)
      pagination.total--
    }
    ElMessage.success('删除成功')
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

.user-page {
  &__header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
    padding-bottom: 10px;
    border-bottom: 1px solid #ebeef5;
  }
  
  &__title {
    font-size: 18px;
    color: #303133;
    font-weight: 500;
    margin: 0;
  }
  
  &__actions {
    display: flex;
    gap: 10px;
  }
  
  &__content {
    background-color: #ffffff;
    border-radius: 4px;
    padding: 20px;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  }
  
  &__toolbar {
    margin-bottom: 20px;
  }
  
  &__search {
    display: flex;
    gap: 16px;
    align-items: center;
    flex-wrap: wrap;
  }
  
  &__pagination {
    margin-top: 20px;
    display: flex;
    justify-content: flex-end;
  }
}
</style>