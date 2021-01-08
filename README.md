# POE 自動喝水放buff

## 功能
- [x] 自動使用藥水以及立即技能，減少操作複雜度，不浪費每瓶藥水作用時間
- [x] 設定為計時自動觸發或按鍵觸發
- [x] 為每隻角色自訂多種規則，隨時切換
- [x] 只在POE遊戲內觸發按鍵
- [ ] 在瀕血或指定血量時使用特定藥水或技能 (預計開發)
- [ ] 獲得特定debuff的時候自動使用相對應的藥水或技能 (預計開發)

## 下載
至[release](https://github.com/shounen51/poe_AutoFlaskByAttack/releases)頁面中下載.zip檔，解壓縮後執行.exe

## 使用與設定
初次使用請先建立第一個設定檔，建議設定檔名稱可以使用角色名稱以方便切換

Del 刪除設定

Esc 取消設定狀態

啟動快捷鍵不支援滑鼠

藥水及buff按鍵必須設定英文字母或數字，無法設定在功能鍵

## 設定檔
目前沒有更改設定檔名稱以及刪除設定檔的功能，~~還沒想到UI要怎樣設計~~

如有以上需求可以自行到./configs/裡刪除或更改.ini的檔名(需先關閉程式)

## 說明
 - 初次開啟程式時如果無法正常作用請重新啟動即可

 - 每次開啟程式時第一次啟動需要以滑鼠點擊啟動按鈕，隨後即可用快捷鍵切換開關

 - 當啟動按鈕為黃色時表示使用者並未在遊戲中，此時不會作用
 
 - 在遊戲中打字的時候一樣會觸發按鍵，請注意不要打亂碼給你的交易對象

 - 任何修改或切換設定檔的動作之前都需要先關閉功能
