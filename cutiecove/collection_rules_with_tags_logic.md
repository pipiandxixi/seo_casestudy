# CutieCove 产品分类规则与标签逻辑

## 标签逻辑说明

在Shopify的Smart Collection规则中，标签判断逻辑有两种：
- **OR逻辑**：满足任一条件，产品包含列出的任何一个标签即可被包含在Collection中
- **AND逻辑**：满足所有条件，产品必须同时包含所有列出的标签才能被包含在Collection中

下表中的"标签逻辑"列说明了每个Collection应使用的判断逻辑。

## 产品分类 Collections

| 分类名称 | 状态 | 标签逻辑 | 建议标签 |
|---------|------|---------|---------|
| Phone & Tech - Phone Cases | existed | OR | **Phone Protection**, **Y2K**, **Japanese Aesthetic**, **Kawaii**, **Trendy Teen**, **Gen Z** |
| Phone & Tech - Airpod Cases | existed | AND+OR | 必须包含:**Phone Protection**<br>可选包含:**Y2K**, **Kawaii**, **Daily Carry** |
| Bags - Totes | existed | AND+OR | 必须包含:**Daily Carry**<br>可选包含:**Travel Essential**, **Eco Friendly** |
| Bags - Crossbody | existed | AND+OR | 必须包含:**Daily Carry**<br>可选包含:**Travel Essential**, **Y2K**, **Minimalist** |
| Bags - Mini Bags | existed | AND+OR | 必须包含:**Bag Charm**<br>可选包含:**Y2K**, **Kawaii**, **Trendy Teen** |
| Bags - Backpacks | existed | AND+OR | 必须包含:**Daily Carry**<br>可选包含:**Back to School**, **College Student**, **Travel Essential** |
| Accessories - Socks | existed | OR | **Y2K**, **Kawaii**, **College Student**, **Trendy Teen**, **Gift** |
| Accessories - Hats & Beanies | existed | AND+OR | 必须包含:**Winter Cozy**<br>可选包含:**Trendy Teen**, **Gen Z** |
| Accessories - Gloves & Mittens | existed | AND+OR | 必须包含:**Winter Cozy**<br>可选包含:**Gift** |
| Accessories - Hair Accessories | existed | OR | **Y2K**, **Kawaii**, **Trendy Teen**, **Aesthetic Lifestyle** |
| Home & Lifestyle - Drinkware | existed | AND+OR | 必须包含:**Stainless Steel**<br>可选包含:**Travel Essential**, **Self Care**, **Daily Carry** |
| Home & Lifestyle - Keychains & Charms | existed | AND+OR | 必须包含:**Bag Charm**或**Everyday Carry Charm**<br>可选包含:**Gift**, **Kawaii**, **Anime Inspired** |
| Home & Lifestyle - Stationary | existed | AND+OR | 必须包含:**Study Buddy**<br>可选包含:**Back to School**, **College Student**, **Gift** |
| Home & Lifestyle - Plush & Figurines | existed | OR | **Kawaii**, **Anime Inspired**, **Gift**, **Animal Theme** |
| Home & Lifestyle - Cozy Decor | existed | AND+OR | 必须包含:**Dorm Decor**或**Winter Cozy**<br>可选包含:**Aesthetic Lifestyle** |
| Home & Lifestyle - Outdoor Fun | existed | OR | **Summer Vibes**, **Travel Essential** |
| Home & Lifestyle | existed | OR | **Gift**, **Self Care**, **Aesthetic Lifestyle**, **Dorm Decor** |
| Tech Accessories | suggested | AND+OR | 必须包含:**Phone Protection**<br>可选包含:**Daily Carry**, **Trendy Teen**, **Gen Z** |
| Winter Accessories | suggested | AND | **Winter Cozy** |

## 风格美学 Collections

| 分类名称 | 状态 | 标签逻辑 | 建议标签 |
|---------|------|---------|---------|
| Y2K Aesthetic | suggested | AND | **Y2K** |
| Japanese Aesthetic | suggested | AND | **Japanese Aesthetic** |
| Kawaii Collection | suggested | AND | **Kawaii** |
| Graffiti & Street Art | suggested | AND | **Graffiti** |
| Minimalist Style | suggested | AND | **Minimalist** |
| Vintage & Retro | suggested | OR | **Vintage**, **Retro** |
| Bohemian Vibes | suggested | AND | **Bohemian** |

## 礼品分类 Collections

| 分类名称 | 状态 | 标签逻辑 | 建议标签 |
|---------|------|---------|---------|
| Gifting - For Her | existed | AND+OR | 必须包含:**Gift**<br>可选包含:**Aesthetic Lifestyle**, **Self Care** |
| Gifting - For Friends | existed | AND+OR | 必须包含:**Gift**<br>可选包含:**Trendy Teen**, **Kawaii** |
| Gifting - Stocking Stuffers | existed | AND+OR | 必须包含:**Gift**和**Under $15**<br>可选包含:**Christmas** |
| Gifting - Under $30 | existed | AND+OR | 必须包含:**Gift**和**Under $25**或**Budget Friendly** |
| Gifting - Christmas Gifts | existed | AND+OR | 必须包含:**Gift**和**Christmas**<br>可选包含:**Winter Cozy** |
| Gifting - Valentine's Gifts | existed | AND+OR | 必须包含:**Gift**和**Valentine** |
| Gifting - For Him | suggested | AND+OR | 必须包含:**Gift**<br>可选包含:**Daily Carry**, **Phone Protection** |
| Gifting - Under $15 | suggested | AND | **Gift**和**Under $15** |
| Gifting - Under $50 | suggested | AND+OR | 必须包含:**Gift**<br>可选包含:**Premium Quality** |
| Gifting - Graduation Gifts | suggested | AND+OR | 必须包含:**Gift**<br>可选包含:**College Student** |
| Gifting - Birthday Gifts | suggested | AND+OR | 必须包含:**Gift**<br>可选包含:**Trendy Teen**, **Gen Z** |

## 新品与热门 Collections

| 分类名称 | 状态 | 标签逻辑 | 建议标签 |
|---------|------|---------|---------|
| New In - This Week | existed | AND | **New Arrival** |
| New In - This Season | existed | AND+OR | 必须包含:**New Arrival**<br>可选包含:当季标签 |
| New In - Trending Now | existed | OR | **Trending Now**, **Viral** |
| Best Sellers | suggested | AND | **Best Seller** |
| Limited Edition | suggested | AND | **Limited Edition** |
| Viral Products | suggested | OR | **Viral**, **Trending Now** |
| Instagram Worthy | suggested | AND+OR | 必须包含:**Instagram Worthy**<br>可选包含:**Aesthetic Lifestyle** |

## 季节性 Collections

| 分类名称 | 状态 | 标签逻辑 | 建议标签 |
|---------|------|---------|---------|
| Sales - Last Chance | existed | 特殊 | 无特定标签 (基于价格或库存) |
| Spring Collection | suggested | AND | **Spring Fresh** |
| Summer Vibes | suggested | AND | **Summer Vibes** |
| Autumn Essentials | suggested | OR | **Earth Tones**, **Winter Cozy** |
| Winter Cozy | suggested | AND+OR | 必须包含:**Winter Cozy**<br>可选包含:**Christmas** |
| Halloween Collection | suggested | AND | **Halloween** |
| Back to School | suggested | AND+OR | 必须包含:**Back to School**<br>可选包含:**College Student**, **Study Buddy** |

## 目标人群 Collections

| 分类名称 | 状态 | 标签逻辑 | 建议标签 |
|---------|------|---------|---------|
| Gen Z Favorites | suggested | AND+OR | 必须包含:**Gen Z**<br>可选包含:**Trendy Teen**, **Y2K** |
| College Essentials | suggested | AND+OR | 必须包含:**College Student**<br>可选包含:**Back to School**, **Study Buddy** |
| Dorm Room Must-Haves | suggested | AND+OR | 必须包含:**Dorm Decor**<br>可选包含:**College Student** |
| Travel Essentials | suggested | AND | **Travel Essential** |
| Self Care Collection | suggested | AND+OR | 必须包含:**Self Care**<br>可选包含:**Aesthetic Lifestyle** |
| Study Buddy | suggested | AND | **Study Buddy** |

## 价格区间 Collections

| 分类名称 | 状态 | 标签逻辑 | 建议标签 |
|---------|------|---------|---------|
| Budget Friendly | suggested | OR | **Budget Friendly**, **Under $15**, **Under $25** |
| Premium Collection | suggested | AND | **Premium Quality** |
| Stocking Stuffers | suggested | AND+OR | 必须包含:**Under $15**和**Gift**<br>可选包含:**Christmas** |

## 主题 Collections

| 分类名称 | 状态 | 标签逻辑 | 建议标签 |
|---------|------|---------|---------|
| Anime Inspired | suggested | AND+OR | 必须包含:**Anime Inspired**<br>可选包含:**Japanese Aesthetic**, **Kawaii** |
| Food Theme | suggested | AND | **Food Theme** |
| Animal Theme | suggested | AND+OR | 必须包含:**Animal Theme**<br>可选包含:**Kawaii** |
| Space & Galaxy | suggested | AND | **Space Theme** |
| Nature & Outdoors | suggested | AND+OR | 必须包含:**Nature Theme**<br>可选包含:**Earth Tones** |
| Sports & Fitness | suggested | AND | **Sports Theme** |
| Art & Creative | suggested | OR | **Creative Professional**, **Aesthetic Lifestyle** |

## 功能性 Collections

| 分类名称 | 状态 | 标签逻辑 | 建议标签 |
|---------|------|---------|---------|
| Phone Protection | suggested | AND | **Phone Protection** |
| Everyday Carry | suggested | OR | **Daily Carry**, **Everyday Carry Charm** |
| Travel Ready | suggested | AND | **Travel Essential** |
| Waterproof Items | suggested | AND | **Waterproof** |
| Eco Friendly | suggested | AND | **Eco Friendly** |
| Personalized Items | suggested | 特殊 | 无特定标签 (基于产品特性) |

## 优先创建建议

| 分类名称 | 状态 | 优先级 | 标签逻辑 | 建议标签 |
|---------|------|-------|---------|---------|
| Y2K Aesthetic | suggested | 高优先级 | AND | **Y2K** |
| Japanese Aesthetic | suggested | 高优先级 | AND | **Japanese Aesthetic** |
| Best Sellers | suggested | 高优先级 | AND | **Best Seller** |
| Kawaii Collection | suggested | 高优先级 | AND | **Kawaii** |
| Tech Accessories | suggested | 中优先级 | AND+OR | 必须包含:**Phone Protection**<br>可选包含:**Daily Carry**, **Trendy Teen**, **Gen Z** |
| Gen Z Favorites | suggested | 中优先级 | AND+OR | 必须包含:**Gen Z**<br>可选包含:**Trendy Teen**, **Y2K** |
| Travel Essentials | suggested | 中优先级 | AND | **Travel Essential** |
| Budget Friendly | suggested | 中优先级 | OR | **Budget Friendly**, **Under $15**, **Under $25** |