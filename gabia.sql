-- 코드를 입력하세요
SELECT C.CART_ID, CASE WHEN TOTAL < C.MINIMUM_REQUIREMENT THEN 1 ELSE 0 END ABUSED
FROM COUPONS AS C
JOIN (SELECT CART_ID, SUM(PRICE) AS TOTAL FROM CART_PRODUCTS GROUP BY CART_ID) AS P
ON C.CART_ID = P.CART_ID
ORDER BY CART_ID