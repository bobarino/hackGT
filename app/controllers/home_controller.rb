class HomeController < ApplicationController
  def index
    @user = current_user
    cur_change = Purchase.where(account_id: @user.account_id).where(ext: true).where(paid: false).pluck(:amt)
    change = 0
    cur_change.each do |num|
      decimal = BigDecimal.new(num.to_s)
      change += 1-decimal.frac
    end
    @cur_change = change
    if @cur_change > 5
      p = Payout.new
      char_array = UserCharity.where(user_id: @user.id)
      char_id = char_array[rand(char_array.length)].charity_id
      p.merchant_id = Charity.find(char_id).merchant_id
      p.account_id = @user.account_id
      p.amt = @cur_change
      p.paid = false
      p.save!
      @cur_change = 0
      Purchase.where(account_id: @user.account_id).where(ext: true).update_all(paid: true)
    end

    donated = Payout.where(account_id: @user.account_id).pluck(:amt)
    total_donated = 0
    donated.each do |don|
      total_donated += don
    end
    @total = total_donated

    port_charities = UserCharity.where(user_id: current_user.id).pluck(:charity_id)
    @charity_list = []
    port_charities.each do |z|
        @charity_list << Charity.find(z).name
    end


    @chart = Fusioncharts::Chart.new({
        width: "600",
        height: "400",
        type: "pie2d",
        renderAt: "chartContainer",
        dataSource: {
            chart: {
            caption: "",
            subCaption: "",
            xAxisname: "",
            yAxisName: "",
            numberPrefix: "$",
            theme: "fint",
            exportEnabled: "1",
            },
            categories: [{
                    category: [
                        { label: "Remaining" },
                        { label: "Donating" }
                    ]
                }],
                dataset: [
                    {
                        seriesname: "Donating",
                        data: [
                            { value: 5-@cur_change },
                            { value: @cur_change }
                        ]
                    },
              ]
        }
    })
  end

  def portfolio
      all_list = Charity.pluck(:name)
      port_charities = UserCharity.where(user_id: current_user.id).pluck(:charity_id)
      @charity_list = []
      port_charities.each do |z|
          @charity_list << Charity.find(z).name
      end
      @not_charity_list = []
      all_list.each do |x|
      flag = true
        @charity_list.each do |y|
          if x == y
            flag = false
          end
        end
        if flag == true
          @not_charity_list << x
        end
      end
    end

  def add_portfolio
    name = params[:name]
    uc = UserCharity.new
    uc.user = current_user
    uc.charity = Charity.where(name: name).first
    uc.save!
    redirect_to portfolio_path
  end
  def finish_portfolio
    current_user.portfolio = true
    current_user.save!
    redirect_to root_path
  end
end
