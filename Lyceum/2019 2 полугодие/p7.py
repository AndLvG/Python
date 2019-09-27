def num2words(num):
    nums_20_90 = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    nums_0_19 = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', "Nine", 'Ten', 'Eleven',
                 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    if num < 20:
        return nums_0_19[num]
    if num < 100:
        return nums_20_90[num // 10 - 2] + ('' if num % 10 == 0 else ' ' + nums_0_19[num % 10])

    return nums_0_19[num // 100] + ' hundred' + (
        '' if num % 100 == 0 else ' and' + (
            '' if num % 100 // 10 == 0 else ' ' + nums_20_90[num % 100 // 10 - 2]) + (
                                      '' if num % 10 == 0 else ' ' + nums_0_19[num % 100 % 10]))


print(num2words(202))
