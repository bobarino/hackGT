class AddMerchantToCharity < ActiveRecord::Migration
  def change
    add_column :charities, :merchant_id, :string
  end
end
