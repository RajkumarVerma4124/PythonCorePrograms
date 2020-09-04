#Given N distinct Coupon Numbers, how many random numbers do you need to generate distinct coupon number

import random
class CouponNumber:
    def main(self):
        countRandom = 0
        try:
            couponCount = int(input("Enter the range of N Distinct coupon do you want : "))
        except ValueError:
            print("Plese provide valid details ! ")
            couponObj.main()
        else:
            couponObj.collectCoupon(couponCount,countRandom)

    def getCouponNumber(self,couponCount):
        return random.randint(1,couponCount)

    def collectCoupon(self,couponCount,countRandom):
        listCoupon = [ ]
        uniqueListCoupon = [ ]
        while (len(uniqueListCoupon) < couponCount):
            for i in range(couponCount):
                couponValue = couponObj.getCouponNumber(couponCount)
                listCoupon.append(couponValue)
                countRandom = countRandom + 1;
                for x in listCoupon:
                    if x not in uniqueListCoupon:
                        uniqueListCoupon.append(x)
        print("The Random No. List Are : ",listCoupon)
        print("The Unique List Are : ",uniqueListCoupon)
        print("The Count Required for getting N Distinct Number are : ",countRandom)

couponObj = CouponNumber()
couponObj.main()