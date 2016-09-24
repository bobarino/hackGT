class AddPortfolioToUser < ActiveRecord::Migration
  def change
    add_column :users, :portfolio, :boolean, :default => false
  end
end
