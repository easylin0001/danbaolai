export interface ListItem {
  id: string
  name: string
  createdAt: string
}

export interface TableColumn {
  prop: string
  label: string
  width?: string | number
  minWidth?: string | number
  sortable?: boolean
  align?: 'left' | 'center' | 'right'
}

export interface Pagination {
  currentPage: number
  pageSize: number
  total: number
}
