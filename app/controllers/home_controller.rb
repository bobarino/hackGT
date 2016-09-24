class HomeController < ApplicationController
  def index
    @user = current_user
  end

  def portfolio
    @charity_list = Charity.pluck(:name)
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
