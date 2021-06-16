interface IObject {
  [key: string]: any
}

interface Option<K = string, V = string> {
  /**
   * 默认为 string
   */
  value: V
  /**
   * 默认为 string
   */
  label: K
}
